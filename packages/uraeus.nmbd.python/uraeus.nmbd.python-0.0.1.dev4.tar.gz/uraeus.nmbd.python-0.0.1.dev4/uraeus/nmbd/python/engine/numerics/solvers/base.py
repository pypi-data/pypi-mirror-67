# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 13:21:35 2019

@author: khale
"""

# Standard library imports.
import sys
import time

# Third party imports.
import numpy as np
import scipy as sc
import pandas as pd
import numba

#from scipy.sparse.linalg import spsolve

# Local imports.
#from ..math_funcs.numba_funcs import matrix_assembler
from ..math_funcs._cython_definitions.matrix_funcs import matrix_assembler

###############################################################################
###############################################################################

@numba.njit(cache=True, nogil=True)
def solve(A, b):
    x = np.linalg.solve(A, b)
    return x


def progress_bar(steps, i, t0, t_sim):
    sys.stdout.write('\r')
    length = (100*(1+i)//(4*steps))
    percentage = 100*(1+i)//steps
    t = time.perf_counter() - t0
    format_ = ('='*length,percentage,i+1, steps, t_sim, t)
    sys.stdout.write("[%-25s] %d%%, (%s/%s) steps. Sim Time = %.5s | CPU Time = %.5s (s)" % format_)
    sys.stdout.flush()

###############################################################################
###############################################################################

class abstract_solver(object):
    
    def __init__(self, model):
        self.model = model
        self._construct_system_arrays()
        self._initialize_model()
        self._create_indicies()
        self._construct_containers()
    
    def _construct_system_arrays(self):
        n  = self.model.n
        nc = self.model.nc
        self._q   = np.zeros((n, 1), dtype=np.float64)
        self._qd  = np.zeros((n, 1), dtype=np.float64)
        self._qdd = np.zeros((n, 1), dtype=np.float64)

        self._lgr = np.zeros((nc, 1), dtype=np.float64)
        #self._pos_m = np.zeros((nc, 1), dtype=np.float64)
        #self._vel_m = np.zeros((nc, 1), dtype=np.float64)
        #self._acc_m = np.zeros((nc, 1), dtype=np.float64)

        self._jac_ = np.zeros((nc, n), dtype=np.float64)
        self._mass = np.zeros((n, n), dtype=np.float64)
        self._mass_matrix_rows = np.arange(self.model.ncols, dtype=np.intc)

        self._coeff_matrix = np.zeros((n + nc, n + nc), dtype=np.float64)
        
        
    def set_initial_states(self, q, qd):
        assert q.shape  == self._q.shape
        assert qd.shape == self._q.shape
        self._set_gen_coordinates(q)
        self._set_gen_velocities(qd)
        self._pos_history[0] = q.copy()
        self._vel_history[0] = qd.copy()

            
    def set_time_array(self, duration, spacing):
        
        if duration > spacing:
            time_array = np.arange(0, duration, spacing)
            step_size  = spacing
        elif duration < spacing:
            time_array, step_size = np.linspace(0, duration, spacing, retstep=True)
        else:
            raise ValueError('Time array is not properly sampled.')
        self.time_array = time_array
        self.step_size  = step_size

        self._construct_containers(time_array.size)
        self.set_initial_states(self.model._q, self.model._qd)
    
    
    def eval_reactions(self):
        self._reactions = {}
        time_array = self.time_array
        bar_length = len(time_array)
        print("\nEvaluating System Constraints' Forces.")
        t0 = time.perf_counter()
        dt = self.step_size
        for i, t in enumerate(time_array):
            # Updating the progress bar
            progress_bar(bar_length, i, t0, t+dt)
            self._set_time(t)
            self._set_gen_coordinates(self._pos_history[i])
            self._set_lagrange_multipliers(self._lgr_history[i])
            reactions = self._eval_reactions_eq()
            self._reactions[i] = reactions
        
        values = {i:np.concatenate(list(v.values())) for i,v in self._reactions.items()}
        
        self.reactions_dataframe = pd.DataFrame(
                data = np.concatenate(list(values.values()),1).T,
                columns = self._reactions_indicies)
        self.reactions_dataframe['time'] = time_array

    
    def _initialize_model(self):
        model = self.model
        model.initialize(self._q, self._qd, self._qdd, self._lgr)

    def _create_indicies(self):
        model = self.model
        sorted_coordinates = {v:k for k,v in model.indicies_map.items()}
        self._coordinates_indicies = []
        for name in sorted_coordinates.values():
            self._coordinates_indicies += ['%s.%s'%(name, i) 
            for i in ['x', 'y', 'z', 'e0', 'e1', 'e2', 'e3']]
            
        self._reactions_indicies = []
        for name in model.reactions_indicies:
            self._reactions_indicies += ['%s.%s'%(name, i) 
            for i in ['x','y','z']]
    
    def _construct_containers(self, size=None):
        self._pos_history = {}#np.empty((size,), dtype=np.ndarray)
        self._vel_history = {}#np.empty((size,), dtype=np.ndarray)
        self._acc_history = {}#np.empty((size,), dtype=np.ndarray)
        self._lgr_history = {}#np.empty((size,), dtype=np.ndarray)

    def _creat_results_dataframes(self):
        columns = self._coordinates_indicies
        constraints = self._reactions_indicies
        
        pos_data = list(self._pos_history.values())
        vel_data = list(self._vel_history.values())
        acc_data = list(self._acc_history.values())
        lgr_data = list(self._lgr_history.values())

        self.pos_dataframe = pd.DataFrame(
                data = np.concatenate(pos_data,1).T,
                columns = columns)
        self.vel_dataframe = pd.DataFrame(
                data = np.concatenate(vel_data,1).T,
                columns = columns)
        self.acc_dataframe = pd.DataFrame(
                data = np.concatenate(acc_data,1).T,
                columns = columns)
        self.lgr_dataframe = pd.DataFrame(
                data = np.concatenate(lgr_data,1).T,
                columns = range(self.model.nc))
        
        time_array = self.time_array
        self.pos_dataframe['time'] = time_array
        self.vel_dataframe['time'] = time_array
        self.acc_dataframe['time'] = time_array
        self.lgr_dataframe['time'] = time_array
    
    def _assemble_equations(self, data):
        mat = np.concatenate(data)
        return mat
    
    def _set_time(self, t):
        self.model.t = t
    
    def _set_gen_coordinates(self, q):
        self._q[:] = q
    
    def _set_gen_velocities(self, qd):
        self._qd[:]  = qd
    
    def _set_gen_accelerations(self, qdd):
        self._qdd[:] = qdd
    
    def _set_lagrange_multipliers(self, lgr):
        self._lgr[:] = lgr

    
    def _eval_pos_eq(self):
        self.model.eval_pos_eq()
        data = self.model.pos_eq_blocks
        mat = self._assemble_equations(data)
        return mat
        
    def _eval_vel_eq(self):
        self.model.eval_vel_eq()
        data = self.model.vel_eq_blocks
        mat  = self._assemble_equations(data)
        return mat
        
    def _eval_acc_eq(self):
        self.model.eval_acc_eq()
        data = self.model.acc_eq_blocks
        mat = self._assemble_equations(data)
        return mat
            
    def _eval_jac_eq(self):
        self.model.eval_jac_eq()
        rows = self.model.jac_rows
        cols = self.model.jac_cols
        data = self.model.jac_eq_blocks
        shape = (self.model.nc, self.model.n)
        matrix_assembler(self._jac_, data, rows, cols, shape)
        return self._jac_
    
    def _eval_mass_eq(self):
        self.model.eval_mass_eq()
        data = self.model.mass_eq_blocks
        n = self.model.n
        rows = cols = self._mass_matrix_rows
        matrix_assembler(self._mass, data, rows, cols, (n, n))
        return self._mass
    
    def _eval_frc_eq(self):
        self.model.eval_frc_eq()
        data = self.model.frc_eq_blocks
        mat = self._assemble_equations(data)
        return mat
        
    def _eval_reactions_eq(self):
        self.model.eval_reactions_eq()
        return self.model.reactions

#    @profile
    def _solve_constraints(self, guess):
        self._set_gen_coordinates(guess)
        
        A = self._eval_jac_eq()
        b = self._eval_pos_eq()
        lu, p = self._factorize_jacobian(A)
        delta_q = sc.linalg.lu_solve((lu, p), -b)
        #delta_q = solve(A, -b)
        
        itr=0
        while np.linalg.norm(delta_q)>1e-4:
#            print(np.linalg.norm(delta_q))
            guess += delta_q
            
            self._set_gen_coordinates(guess)
            b = self._eval_pos_eq()
            delta_q = sc.linalg.lu_solve((lu, p), -b)
            
            if (itr % 10) == 0 and itr != 0:
                #print('Updating Jacobian\n')
                A = self._eval_jac_eq()
                lu, p = self._factorize_jacobian(A)
                delta_q = sc.linalg.lu_solve((lu, p), -b)
            if itr > 50:
                print("Iterations exceded \n")
                #raise ValueError("Iterations exceded \n")
                break
            itr+=1
        self._jac = self._eval_jac_eq()

    def _factorize_jacobian(self, jacobian):
        lu, p = sc.linalg.lu_factor(jacobian)
        return lu, p


