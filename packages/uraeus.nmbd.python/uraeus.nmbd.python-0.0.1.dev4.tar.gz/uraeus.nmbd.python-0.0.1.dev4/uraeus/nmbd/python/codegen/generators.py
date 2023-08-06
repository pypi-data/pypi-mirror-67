# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 13:23:39 2019

@author: khale
"""

# Standard library imports
import os
import re
import textwrap
import itertools

# Local application imports
from .printer import npsc_printer as printer


class abstract_generator(object):
    """
    A python code-generator class that generates numerical code with an OOP
    structure.
    
    Parameters
    ----------
    mbs : topology
        An instance of a topology class.
    
    Methods
    -------
    write_code_file()
        Write the structured code-files in a .py file format. These code-files
        are saved in the corresponding sub-directory in the //generated_templates
        directory.
        
    Notes
    -----
    This generator structures the numerical code of the system as follows:
        - Creating a 'model_name'.py file that is designed  be used as an 
          imported  module. The file is saved in a sub-directory inside the
          'generated_templates' directory.
        - This module contains one class only, the 'topology' class.
        - This class provides the interface to be used either directly by the 
          python_solver or indirectly by the assembly class that assembles 
          several 'topology' classes together.

    """
    
    def __init__(self, mbs, _printer=printer()):
        
        self.mbs     = mbs
        self.printer = _printer
        self.name    = self.mbs.name
                
        self.arguments_symbols = [self.printer._print(exp) for exp in self.mbs.arguments_symbols]
        self.constants_symbols = [self.printer._print(exp) for exp in self.mbs.constants_symbols]
        self.runtime_symbols   = [self.printer._print(exp) for exp in self.mbs.runtime_symbols]
        
        self.primary_arguments = self.arguments_symbols
        
        self.constants_symbolic_expr = self.mbs.constants_symbolic_expr
        self.constants_numeric_expr  = self.mbs.constants_numeric_expr
        
        self.gen_coordinates_exp = self.mbs.mapped_gen_coordinates
        self.gen_coordinates_sym = [self.printer._print(exp.lhs) for exp in self.gen_coordinates_exp]

        self.gen_velocities_exp  = self.mbs.mapped_gen_velocities
        self.gen_velocities_sym  = [self.printer._print(exp.lhs) for exp in self.gen_velocities_exp]
        
        self.gen_accelerations_exp  = self.mbs.mapped_gen_accelerations
        self.gen_accelerations_sym  = [self.printer._print(exp.lhs) for exp in self.gen_accelerations_exp]
        
        self.lagrange_multipliers_exp  = self.mbs.mapped_lagrange_multipliers
        self.lagrange_multipliers_sym  = [self.printer._print(exp.lhs) for exp in self.lagrange_multipliers_exp]

        self.joint_reactions_sym = [self.printer._print(exp) for exp in self.mbs.reactions_symbols]

        self.virtual_coordinates = [self.printer._print(exp) for exp in self.mbs.virtual_coordinates]
                
        self.bodies = self.mbs.bodies

    @staticmethod
    def _insert_string(string):
        def inserter(x): return string + x.group(0)
        return inserter

###############################################################################
###############################################################################

class template_codegen(abstract_generator):
    
    def write_imports(self):
        text = '''
                import numpy as np
                from numpy import cos, sin
                from scipy.misc import derivative
                
                from uraeus.nmbd.python.engine.numerics.math_funcs import A, B, G, E, triad, skew, multi_dot
                
                # CONSTANTS
                F64_DTYPE = np.float64

                I1 = np.eye(1, dtype=F64_DTYPE)
                I2 = np.eye(2, dtype=F64_DTYPE)
                I3 = np.eye(3, dtype=F64_DTYPE)
                I4 = np.eye(4, dtype=F64_DTYPE)

                Z1x1 = np.zeros((1,1), F64_DTYPE)
                Z1x3 = np.zeros((1,3), F64_DTYPE)
                Z3x1 = np.zeros((3,1), F64_DTYPE)
                Z3x4 = np.zeros((3,4), F64_DTYPE)
                Z4x1 = np.zeros((4,1), F64_DTYPE)
                Z4x3 = np.zeros((4,3), F64_DTYPE)
                '''
        text = text.expandtabs()
        text = textwrap.dedent(text)
        return text
        
    def write_class_init(self):
        text = '''
                class topology(object):

                    def __init__(self,prefix=''):
                        self.t = 0.0
                        self.prefix = (prefix if prefix=='' else prefix+'.')
                        self.config = None
                        
                        self.indicies_map = {indicies_map}
                        
                        self.n  = {n}
                        self.nc = {nc}
                        self.nrows = {nve}
                        self.ncols = 2*{nodes}
                        self.rows = np.arange(self.nrows, dtype=np.intc)
                        
                        reactions_indicies = {reactions}
                        self.reactions_indicies = ['%s%s'%(self.prefix,i) for i in reactions_indicies]
                '''
        text = text.expandtabs()
        text = textwrap.dedent(text)
                
        reactions = ['%s'%i for i in self.joint_reactions_sym]

        text = text.format(n = self.mbs.n,
                           nc = self.mbs.nc,
                           nve = self.mbs.nve,
                           nodes = len(self.mbs.bodies),
                           reactions = reactions,
                           indicies_map  = self.mbs.nodes_indicies)
        return text

    def write_template_assembler(self):
        text = '''
                def initialize(self, q, qd, qdd, lgr):
                    self.t = 0
                    self.assemble(self.indicies_map, {{}}, 0)
                    self._set_states_arrays(q, qd, qdd, lgr)
                    self._map_states_arrays()
                    self.set_initial_states()
                    self.eval_constants()
                                
                def assemble(self, indicies_map, interface_map, rows_offset):
                    self.rows_offset = rows_offset
                    self._set_mapping(indicies_map, interface_map)
                    self.rows += self.rows_offset
                    self.jac_rows = np.array({jac_rows}, dtype=np.intc)
                    self.jac_rows += self.rows_offset
                    self.jac_cols = np.array([{jac_cols}], dtype=np.intc)
                
                def _set_states_arrays(self, q, qd, qdd, lgr):
                    self._q = q
                    self._qd = qd
                    self._qdd = qdd
                    self._lgr = lgr
                
                def _map_states_arrays(self):
                    self._map_gen_coordinates()
                    self._map_gen_velocities()
                    self._map_gen_accelerations()
                    self._map_lagrange_multipliers()
                
                def set_initial_states(self):
                    np.concatenate([{coordinates}], out=self._q)

                    np.concatenate([{velocities}], out=self._qd)
                    
                def _set_mapping(self,indicies_map, interface_map):
                    p = self.prefix
                    {maped}
                    {virtuals}
               '''
        
        indent = 4*' '
        text = text.expandtabs()
        text = textwrap.dedent(text)
        
        nodes = '\n'.join(['%s = indicies_map[p + %r]'%('self.%s'%i,i) for i in self.bodies])
        nodes = textwrap.indent(nodes,indent).lstrip()
        
        virtuals = '\n'.join(['%s = indicies_map[interface_map[p + %r]]'%('self.%s'%i,i) for i in self.mbs.virtual_bodies])
        virtuals = textwrap.indent(virtuals,indent).lstrip()
        
        ind_body = {v:k for k,v in self.mbs.nodes_indicies.items()}
        rows, cols, data = zip(*self.mbs.jac_equations.row_list())
        string_cols = [('self.%s*2'%ind_body[i//2] if i%2==0 else 'self.%s*2+1'%ind_body[i//2]) for i in cols]
        string_cols_text = ', '.join(string_cols)

        self_inserter  = self._insert_string('self.config.')
        pattern = '|'.join(self.runtime_symbols)

        coordinates = ',\n'.join(self.gen_coordinates_sym)
        coordinates = re.sub(pattern,self_inserter,coordinates)
        coordinates = (coordinates if len(coordinates)!=0 else '[]')
        coordinates = textwrap.indent(coordinates,indent).lstrip()
        
        velocities = ',\n'.join(self.gen_velocities_sym)
        velocities = re.sub(pattern,self_inserter,velocities)
        velocities = (velocities if len(velocities)!=0 else '[]')
        velocities = textwrap.indent(velocities,indent).lstrip()
        
        text = text.format(maped = nodes,
                           virtuals = virtuals,
                           jac_rows = list(rows),
                           jac_cols = string_cols_text,
                           coordinates = coordinates,
                           velocities = velocities)
        text = textwrap.indent(text,indent)
        return text
    
    def write_constants_eval(self):
        text = '''
                def eval_constants(self):
                    config = self.config
                    
                    {num_constants}
                    
                    {sym_constants}
                '''
        text = text.expandtabs()
        text = textwrap.dedent(text)
        
        printer = self.printer
        indent = 4*' '
                
        config_pattern_iter = itertools.chain(self.arguments_symbols,
                                              self.virtual_coordinates)
        config_pattern = '|'.join(config_pattern_iter)
        config_inserter = self._insert_string('config.')
        
        self_pattern_iter = itertools.chain(self.constants_symbols)
        self_pattern = '|'.join(self_pattern_iter)
        self_inserter = self._insert_string('self.')
        
        sym_constants = self.constants_symbolic_expr
        sym_constants_text = '\n'.join((printer._print(i) for i in sym_constants))
        sym_constants_text = re.sub(config_pattern, config_inserter, sym_constants_text)
        sym_constants_text = re.sub(self_pattern, self_inserter, sym_constants_text)
        sym_constants_text = textwrap.indent(sym_constants_text, indent).lstrip()
        
        num_constants_list = self.constants_numeric_expr
        num_constants_text = '\n'.join((printer._print(i) for i in num_constants_list))
        num_constants_text = re.sub(config_pattern, config_inserter, num_constants_text)
        num_constants_text = re.sub(self_pattern, self_inserter, num_constants_text)
        num_constants_text = textwrap.indent(num_constants_text, indent).lstrip()

        text = text.expandtabs()
        text = textwrap.dedent(text)
        text = text.format(sym_constants = sym_constants_text,
                           num_constants = num_constants_text)
        text = textwrap.indent(text,indent)
        return text

    def write_coordinates_setter(self):
        return self._write_x_mapper('gen_coordinates','q')
    
    def write_velocities_setter(self):
        return self._write_x_mapper('gen_velocities','qd')
    
    def write_accelerations_setter(self):
        return self._write_x_mapper('gen_accelerations','qdd')
    
    def write_lagrange_setter(self):
        return self._write_x_mapper('lagrange_multipliers','Lambda')
        
    def write_pos_equations(self):
        return self._write_x_equations('pos')
    
    def write_vel_equations(self):
        return self._write_x_equations('vel')
    
    def write_acc_equations(self):
        return self._write_x_equations('acc')
    
    def write_jac_equations(self):
        return self._write_x_equations('jac')
    
    def write_forces_equations(self):
        return self._write_x_equations('frc')
    
    def write_mass_equations(self):
        return self._write_x_equations('mass')
    
    def write_reactions_equations(self):
        text = '''
                def eval_reactions_eq(self):
                    config  = self.config
                    t = self.t
                    
                    {equations_text}
                    
                    self.reactions = {reactions}
                '''
        text = text.expandtabs()
        text = textwrap.dedent(text)
        
        indent = 4*' '
        p = self.printer
        
        equations = self.mbs.reactions_equalities
        equations_text = '\n'.join([p._print(expr) for expr in equations])
        
        self_pattern = itertools.chain(self.runtime_symbols,
                                       self.constants_symbols,
                                       self.joint_reactions_sym,
                                       self.lagrange_multipliers_sym)
        self_pattern = '|'.join(self_pattern)
        self_inserter = self._insert_string('self.')
        equations_text = re.sub(self_pattern,self_inserter,equations_text)
        
        config_pattern = set(self.primary_arguments) - set(self.runtime_symbols)
        config_pattern = '|'.join([r'%s'%i for i in config_pattern])
        config_inserter = self._insert_string('config.')
        equations_text = re.sub(config_pattern,config_inserter,equations_text)
                
        equations_text = textwrap.indent(equations_text,indent).lstrip() 
        
        reactions = ',\n'.join(['%r : self.%s'%(i,i) for i in self.joint_reactions_sym])
        reactions = textwrap.indent(reactions, 5*indent).lstrip()
        reactions = '{%s}'%reactions
        
        text = text.format(equations_text = equations_text,
                           reactions = reactions)
        text = textwrap.indent(text,indent)
        return text


    def write_system_class(self):
        text = '''
                {class_init}
                    {assembler}
                    {constants}
                    {coord_setter}
                    {veloc_setter}
                    {accel_setter}
                    {lagrg_setter}
                    {eval_pos}
                    {eval_vel}
                    {eval_acc}
                    {eval_jac}
                    {eval_mass}
                    {eval_frc}
                    {eval_rct}
                '''
        text = text.expandtabs()
        text = textwrap.dedent(text)
        
        class_init = self.write_class_init()
        assembler  = self.write_template_assembler()
        constants  = self.write_constants_eval()
        coord_setter = self.write_coordinates_setter()
        veloc_setter = self.write_velocities_setter()
        accel_setter = self.write_accelerations_setter()
        lagrg_setter = self.write_lagrange_setter()
        
        eval_pos = self.write_pos_equations()
        eval_vel = self.write_vel_equations()
        eval_acc = self.write_acc_equations()
        eval_jac = self.write_jac_equations()
        eval_frc = self.write_forces_equations()
        eval_mass = self.write_mass_equations()
        eval_rct = self.write_reactions_equations()
        
        text = text.format(class_init = class_init,
                           assembler = assembler,
                           constants = constants,
                           eval_pos = eval_pos,
                           eval_vel = eval_vel,
                           eval_acc = eval_acc,
                           eval_jac = eval_jac,
                           eval_frc = eval_frc,
                           eval_rct = eval_rct,
                           eval_mass = eval_mass,
                           coord_setter = coord_setter,
                           veloc_setter = veloc_setter,
                           accel_setter = accel_setter,
                           lagrg_setter = lagrg_setter)
        return text
    
    
    def write_code_file(self, dir_path=''):
        file_path = os.path.join(dir_path, self.name)
        imports = self.write_imports()
        system_class = self.write_system_class()
        text = '\n'.join([imports,system_class])
        with open('%s.py'%file_path, 'w') as file:
            file.write(text)
        print('File full path : %s.py'%file_path)
    
    ###########################################################################
    ###########################################################################

    def _write_x_mapper(self, func_name, var):
        text = '''
                def _map_%s(self):
                    %s = self._%s
                    {equalities}
               '''%(func_name, var, 'lgr' if var == 'Lambda' else var)
        
        text = text.expandtabs()
        text = textwrap.dedent(text)
        
        p = self.printer
        indent = 4*' '
        
        symbolic_equality  = getattr(self,'%s_exp'%func_name)
        
        if len(symbolic_equality) !=0:
            pattern = '|'.join(getattr(self,'%s_sym'%func_name))
            self_inserter = self._insert_string('self.')
            
            numerical_equality = '\n'.join([p._print(i) for i in symbolic_equality])
            numerical_equality = re.sub(pattern,self_inserter,numerical_equality)
            numerical_equality = textwrap.indent(numerical_equality,indent).lstrip()
        else:
            numerical_equality = 'pass'
        
        text = text.format(equalities = numerical_equality)
        text = textwrap.indent(text,indent)
        return text
    
    def _write_x_equations(self, eq_initial):
        text = '''
                def eval_{eq_initial}_eq(self):
                    config = self.config
                    t = self.t

                    {replacements}

                    self.{eq_initial}_eq_blocks = ({expressions},)
                '''
        
        text = text.expandtabs()
        text = textwrap.dedent(text)
        
        printer = self.printer
        indent = 4*' '
                
        # Geting the optimized equations' vector/matrix from the topology class.
        # The expected format is two lists [replacements] and [expressions].
        replacements_list = getattr(self.mbs,'%s_rep'%eq_initial)
        expressions_list  = getattr(self.mbs,'%s_exp'%eq_initial)
        # Extracting the vector/matrix from the returned expressions list.
        vector_expr = expressions_list[0]
        # Extracting the Non-Zero values of the vector/matrix.
        vector_data = [i[-1] for i in vector_expr.row_list()]
        
        # Extract the numerical format of the replacements and expressions into
        # a list of string expressions.
        num_repl_list = [printer._print(exp) for exp in replacements_list]
        num_expr_list = [printer._print(exp) for exp in vector_data]
        
        # Joining the extracted strings to form a valid text block.
        num_repl_text = '\n'.join(num_repl_list)
        num_expr_text = ',\n'.join(num_expr_list) if len(num_expr_list) != 0 else '[]'

        # Creating a regex pattern of strings that represents the variables
        # which need to be perfixed by a 'self.' to be referenced correctly.
        self_pattern = itertools.chain(self.runtime_symbols,
                                       self.constants_symbols)
        self_pattern = '|'.join(self_pattern)
        
        # Creating a regex pattern of strings that represents the variables
        # which need to be perfixed by a 'config.' to be referenced correctly.
        config_pattern = set(self.primary_arguments) - set(self.runtime_symbols)
        config_pattern = '|'.join([r'%s'%i for i in config_pattern])
        
        # Performing the regex substitution with 'self.'.
        self_inserter = self._insert_string('self.')
        num_repl_text = re.sub(self_pattern,self_inserter,num_repl_text)
        num_expr_text = re.sub(self_pattern,self_inserter,num_expr_text)
        
        # Performing the regex substitution with 'config.'.
        config_inserter = self._insert_string('config.')
        num_repl_text = re.sub(config_pattern,config_inserter,num_repl_text)
        num_expr_text = re.sub(config_pattern,config_inserter,num_expr_text)
        
        # Indenting the text block for propper class and function indentation.
        num_repl_text = textwrap.indent(num_repl_text,indent).lstrip() 
        num_expr_text = textwrap.indent(num_expr_text,indent).lstrip()
        
        text = text.format(eq_initial  = eq_initial,
                           replacements = num_repl_text,
                           expressions  = num_expr_text)
        text = textwrap.indent(text,indent)
        return text
    

###############################################################################
###############################################################################

def flatten_assembly(assm, attr):
    if len(assm.assemblies) == 0:
        return getattr(assm, attr)
    else:
        nested = {}
        for _assm in assm.assemblies.values():
            nested.update(flatten_assembly(_assm, attr))
        nested.update(getattr(assm, attr))
        return nested

def flatten_equalities(assm, attr):
    if len(assm.assemblies) == 0:
        return getattr(assm, attr)
    else:
        nested = []
        for _assm in assm.assemblies.values():
            nested += flatten_equalities(_assm, attr)
        nested += getattr(assm, attr)
        return nested

class assembly_codegen(template_codegen):
    
    def __init__(self, multibody_system, printer=printer()):
        self.mbs  = multibody_system
        self.printer = printer
        
        self._interface_assembly_instance()
        
        self.templates = []
        self.subsystems_templates = {}
        
        for sub_name, system in self.subsystems.items():
            topology_name = system.template.name
            self.subsystems_templates[sub_name] = topology_name
            if topology_name not in self.templates:
                self.templates.append(topology_name)
    
    
    def _interface_assembly_instance(self):
        mbs = self.mbs
        self.name = mbs.name
        self.subsystems    = flatten_assembly(mbs, 'subsystems')
        self.interface_map = flatten_assembly(mbs, 'interface_map')
        self.nodes_indicies = mbs.nodes_indicies
        self.mapped_gen_coordinates = flatten_equalities(mbs, 'mapped_gen_coordinates')
        self.mapped_vir_coordinates = flatten_equalities(mbs, 'mapped_vir_coordinates')
        self.mapped_gen_velocities  = flatten_equalities(mbs, 'mapped_gen_velocities')
        self.mapped_vir_velocities  = flatten_equalities(mbs, 'mapped_vir_velocities')
        self.mapped_gen_accelerations = flatten_equalities(mbs, 'mapped_gen_accelerations')
        self.mapped_vir_accelerations = flatten_equalities(mbs, 'mapped_vir_accelerations')
    
        
    def write_imports(self):
        text = '''
                import itertools
                
                import numpy as np
                from numpy.linalg import multi_dot
                
                from uraeus.nmbd.python.numerics.core.math_funcs import G
                                
                {templates_imports}
                
                class subsystems(object):
                    {subsystems}
                '''
        indent = 4*' '
        tpl_import_prefix = 'from ..templates'
        templates_imports = '\n'.join(['%s import %s'%(tpl_import_prefix, i)
                                        for i in self.templates])
        
        subsystems = ['%s = %s.topology(%r)'%(subsys, template, subsys)\
                      for subsys, template in self.subsystems_templates.items()]
            
        subsystems = '\n'.join(subsystems)
        subsystems = textwrap.dedent(subsystems)
        subsystems = textwrap.indent(subsystems,indent).lstrip()
        text = text.expandtabs()
        text = textwrap.dedent(text)
        text = text.format(templates_imports = templates_imports,
                           subsystems = subsystems)
        return text
    
    def write_class_init(self):
        text = '''
                class topology(object):

                    def __init__(self):
                        self._t = 0
                        self.subsystems = [{subsystems}]
                        
                        self.nrows = sum([sub.nrows for sub in self.subsystems]) + 2
                        self.ncols = sum([sub.ncols for sub in self.subsystems]) + 2

                        self.interface_map = {interface_map}
                        self.indicies_map  = {indicies_map}
                        
                        self.R_ground  = np.array([[0],[0],[0]], dtype=F64_DTYPE)
                        self.P_ground  = np.array([[1],[0],[0],[0]], dtype=F64_DTYPE)
                        self.Pg_ground = np.array([[1],[0],[0],[0]], dtype=F64_DTYPE)
                        
                        self.m_ground = I3
                        self.Jbar_ground = I3
                        
                        self.gr_rows = np.array([0,1], dtype=np.intc)
                        self.gr_jac_rows = np.array([0,0,1,1], dtype=F64_DTYPE)
                        self.gr_jac_cols = np.array([0,1,0,1], dtype=F64_DTYPE)
                        
                        self.n  = sum([sub.n for sub in self.subsystems]) + 7
                        self.nc = sum([sub.nc for sub in self.subsystems]) + 7
                '''
        
        subsystems = ','.join(['subsystems.%s'%i for i in self.subsystems.keys()])
        interface_map = self.interface_map
        indicies_map  = self.nodes_indicies
        text = text.expandtabs()
        text = textwrap.dedent(text)
        text = text.format(subsystems = subsystems,
                           interface_map = interface_map,
                           indicies_map  = indicies_map)
        return text

    def write_class_helpers(self):
        text = '''
                @property
                def t(self):
                    return self._t
                @t.setter
                def t(self,t):
                    self._t = t
                    for sub in self.subsystems:
                        sub.t = t
                
                def set_initial_states(self):
                    for sub in self.subsystems:
                        sub.set_initial_states()
                    coordinates = [sub.q0 for sub in self.subsystems if len(sub.q0)!=0]
                    self.q0 = np.concatenate([self.R_ground,self.P_ground,*coordinates])
                
                def initialize(self):
                    self.t = 0
                    self.assemble()
                    self.set_initial_states()
                    self.eval_constants()
                '''
        indent = 4*' '
        text = text.expandtabs()
        text = textwrap.dedent(text)
        text = textwrap.indent(text,indent).lstrip()
        return text
    
    def write_assembler(self):
        text = '''
                def assemble(self):
                    offset = 2
                    for sub in self.subsystems:
                        sub.assemble(self.indicies_map, self.interface_map, offset)
                        offset += sub.nrows
                                        
                    self.rows = np.concatenate([s.rows for s in self.subsystems])
                    self.jac_rows = np.concatenate([s.jac_rows for s in self.subsystems])
                    self.jac_cols = np.concatenate([s.jac_cols for s in self.subsystems])
            
                    self.rows = np.concatenate([self.gr_rows,self.rows])
                    self.jac_rows = np.concatenate([self.gr_jac_rows,self.jac_rows])
                    self.jac_cols = np.concatenate([self.gr_jac_cols,self.jac_cols])
                    
                    self.reactions_indicies = sum([sub.reactions_indicies for sub in self.subsystems],[])
               '''
        indent = 4*' '
        text = text.expandtabs()
        text = textwrap.dedent(text)
        text = textwrap.indent(text,indent).lstrip()
        return text
        
    def write_constants_evaluator(self):
        text = '''
                def eval_constants(self):
                    {subsystems}
                    {virtuals_map}
                    
                    for sub in self.subsystems:
                        sub.eval_constants()
                '''
        indent = 4*' '
        p = self.printer
        text = text.expandtabs()
        text = textwrap.dedent(text)
        
        subsystems = '\n'.join(['%s = subsystems.%s'%(i,i) for i in self.subsystems.keys()])
        subsystems = textwrap.dedent(subsystems)
        subsystems = textwrap.indent(subsystems,indent).lstrip()

        ground_map = self.mapped_gen_coordinates[0:2]
        pattern = '|'.join([p._print(i.lhs) for i in ground_map])

        virtuals_map = self.mapped_vir_coordinates
        pattern1 = '|'.join([p._print(i.lhs) for i in virtuals_map])
        pattern2 = '|'.join([p._print(i.rhs) for i in virtuals_map])
        
        def sub(x):
            l = x.group(0).split('.')
            try:
                s = '%s.config.%s'%(*l,)
            except TypeError:
                s = '%s'%x.group(0)
            return s
        self_inserter = self._insert_string('self.')
        
        virtuals_map = '\n'.join([p._print(expr) for expr in virtuals_map])
        virtuals_map = re.sub(pattern,self_inserter,virtuals_map)
        virtuals_map = re.sub(pattern1,sub,virtuals_map)
        virtuals_map = re.sub(pattern2,sub,virtuals_map)
        virtuals_map = textwrap.indent(virtuals_map,indent).lstrip()
        
        text = text.format(subsystems = subsystems ,
                           virtuals_map = virtuals_map)
        text = textwrap.indent(text,indent)
        return text
    
    def write_coordinates_setter(self):
        return self._write_x_setter('coordinates','q')
    
    def write_velocities_setter(self):
        return self._write_x_setter('velocities','qd')
    
    def write_accelerations_setter(self):
        return self._write_x_setter('accelerations','qdd')
    
    def write_lagrange_setter(self):
        func_name = 'lagrange_multipliers'
        var = 'Lambda'
        text = '''
                def set_{func_name}(self,{var}):
                    offset = 7
                    for sub in self.subsystems:
                        l = {var}[offset:sub.nc+offset]
                        sub.set_{func_name}(l)
                        offset += sub.nc
               '''
        indent = 4*' '
        text = text.expandtabs()
        text = textwrap.dedent(text)
        text = text.format(func_name = func_name,
                           var = var)
        text = textwrap.indent(text,indent)
        return text
        
    def write_pos_equations(self):
        return self._write_x_equations('pos')
    
    def write_vel_equations(self):
        return self._write_x_equations('vel')
    
    def write_acc_equations(self):
        return self._write_x_equations('acc')
    
    def write_jac_equations(self):
        return self._write_x_equations('jac')
    
    def write_forces_equations(self):
        return self._write_x_equations('frc')
    
    def write_mass_equations(self):
        return self._write_x_equations('mass')

    def write_reactions_equations(self):
        func_name = 'reactions'
        text = '''
                def eval_{func_name}_eq(self):
                    self.reactions = {{}}
                    for sub in self.subsystems:
                        sub.eval_reactions_eq()
                        for k,v in sub.reactions.items():
                            self.reactions['%s%s'%(sub.prefix,k)] = v
                '''
        indent = 4*' '
        text = text.expandtabs()
        text = textwrap.dedent(text)
        
        text = text.format(func_name = func_name)
        text = textwrap.indent(text, indent)
        return text
    
    
    def write_system_class(self):
        text = '''
                {class_init}
                    {class_helpers}
                    {assembler}
                    {constants}
                    {coord_setter}
                    {veloc_setter}
                    {accel_setter}
                    {lagrg_setter}
                    {eval_pos}
                    {eval_vel}
                    {eval_acc}
                    {eval_jac}
                    {eval_mass}
                    {eval_frc}
                    {eval_rct}
                '''
        text = text.expandtabs()
        text = textwrap.dedent(text)
        
        class_init = self.write_class_init()
        class_helpers = self.write_class_helpers()
        assembler = self.write_assembler()
        constants = self.write_constants_evaluator()
        coord_setter = self.write_coordinates_setter()
        veloc_setter = self.write_velocities_setter()
        accel_setter = self.write_accelerations_setter()
        lagrg_setter = self.write_lagrange_setter()
        
        eval_pos = self.write_pos_equations()
        eval_vel = self.write_vel_equations()
        eval_acc = self.write_acc_equations()
        eval_jac = self.write_jac_equations()
        eval_frc = self.write_forces_equations()
        eval_mass = self.write_mass_equations()
        eval_rct = self.write_reactions_equations()
        
        text = text.format(class_init = class_init,
                           class_helpers = class_helpers,
                           assembler = assembler,
                           constants = constants,
                           eval_pos = eval_pos,
                           eval_vel = eval_vel,
                           eval_acc = eval_acc,
                           eval_jac = eval_jac,
                           eval_frc = eval_frc,
                           eval_rct = eval_rct,
                           eval_mass = eval_mass,
                           coord_setter = coord_setter,
                           veloc_setter = veloc_setter,
                           accel_setter = accel_setter,
                           lagrg_setter = lagrg_setter)
        return text
    
    
    def write_code_file(self, dir_path=''):
        file_path = os.path.join(dir_path, self.name)
        imports = self.write_imports()
        system_class = self.write_system_class()
        text = ''.join([imports, system_class])
        with open('%s.py'%file_path, 'w') as file:
            file.write(text)
        print('File full path : %s.py'%file_path)

    ###########################################################################
    def _write_x_setter(self,func_name,var='q'):
        text = '''
                def set_gen_{func_name}(self,{var}):
                    {ground_map}
                    offset = 7
                    for sub in self.subsystems:
                        qs = {var}[offset:sub.n+offset]
                        sub.set_gen_{func_name}(qs)
                        offset += sub.n
                      
                    {subsystems}
                    {virtuals_map}
               '''
        indent = 4*' '
        p = self.printer
        text = text.expandtabs()
        text = textwrap.dedent(text)
        
        self_inserter = self._insert_string('self.')
        
        ground_map = getattr(self,'mapped_gen_%s'%func_name)[0:2]
        pattern = '|'.join([p._print(i.lhs) for i in ground_map])
        ground_map = '\n'.join([p._print(i) for i in ground_map])
        ground_map = re.sub(pattern,self_inserter,ground_map)
        ground_map = textwrap.indent(ground_map,indent).lstrip()

        subsystems = '\n'.join(['%s = subsystems.%s'%(i,i) for i in self.subsystems.keys()])
        subsystems = textwrap.dedent(subsystems)
        subsystems = textwrap.indent(subsystems,indent).lstrip()

        virtuals_map = getattr(self,'mapped_vir_%s'%func_name)
        pattern1 = '|'.join([p._print(i.lhs) for i in virtuals_map])
        pattern2 = '|'.join([p._print(i.rhs) for i in virtuals_map])
        sub = self._insert_string('')
        virtuals_map = '\n'.join([str(p._print(i)) for i in virtuals_map])
        virtuals_map = re.sub(pattern,self_inserter,virtuals_map)
        virtuals_map = re.sub(pattern1,sub,virtuals_map)
        virtuals_map = re.sub(pattern2,sub,virtuals_map)
        virtuals_map = textwrap.indent(virtuals_map,indent).lstrip()
                
        text = text.format(func_name = func_name,
                           var = var,
                           ground_map = ground_map,
                           virtuals_map = virtuals_map,
                           subsystems = subsystems)
        text = textwrap.indent(text,indent)
        return text
    
    
    def _write_x_equations(self,func_name):
        text = '''
                def eval_{func_name}_eq(self):
                    {ground_data}
                    
                    for sub in self.subsystems:
                        sub.eval_{func_name}_eq()
                    
                    eq_blocks = (s.{func_name}_eq_blocks for s in self.subsystems)
                    
                    self.{func_name}_eq_blocks = (*{func_name}_ground_eq_blocks, *itertools.chain(*eq_blocks))
                '''
        
        indent = 4*' '
        p = self.printer
        text = text.expandtabs()
        text = textwrap.dedent(text)
        
        matrix = p._print(getattr(self.mbs,'%s_equations'%func_name)).split('\n')
        rows, cols, ground_data = matrix
        
        symbols = itertools.chain(self.mbs.nodes['ground']['arguments_symbols'],
                                  self.mbs.nodes['ground']['constants_symbols'])
        pattern = '|'.join([p._print(i) for i in symbols])
        self_inserter = self._insert_string('self.')
        ground_data = re.sub(pattern, self_inserter, ground_data)
                
        ground_data = textwrap.indent(ground_data,indent).lstrip()
        ground_data = '%s_ground_eq_blocks = %s'%(func_name,ground_data.lstrip())
        
        text = text.format(func_name = func_name,
                           ground_data = ground_data)
        text = textwrap.indent(text,indent)
        return text

###############################################################################
###############################################################################

class assembly_codegen2(abstract_generator):
    
    def __init__(self, multibody_system, printer=printer()):
        self.mbs  = multibody_system
        self.printer = printer
        
        self._interface_assembly_instance()
        
        self.templates = []
        self.subsystems_templates = {}
        
        for sub_name, system in self.subsystems.items():
            topology_name = system.template.name
            self.subsystems_templates[sub_name] = topology_name
            if topology_name not in self.templates:
                self.templates.append(topology_name)
    
    
    def _interface_assembly_instance(self):
        mbs = self.mbs
        self.name = mbs.name
        self.subsystems    = flatten_assembly(mbs, 'subsystems')
        self.interface_map = flatten_assembly(mbs, 'interface_map')
        self.nodes_indicies = mbs.nodes_indicies
        self.mapped_gen_coordinates = flatten_equalities(mbs, 'mapped_gen_coordinates')
        self.mapped_vir_coordinates = flatten_equalities(mbs, 'mapped_vir_coordinates')
        self.mapped_gen_velocities  = flatten_equalities(mbs, 'mapped_gen_velocities')
        self.mapped_vir_velocities  = flatten_equalities(mbs, 'mapped_vir_velocities')
        self.mapped_gen_accelerations = flatten_equalities(mbs, 'mapped_gen_accelerations')
        self.mapped_vir_accelerations = flatten_equalities(mbs, 'mapped_vir_accelerations')
    
        
    def write_imports(self):
        text = '''
                import numpy as np
                from smbd.numenv.python.numerics.numcls import num_assm

                {templates_imports}
                
                class subsystems(object):
                    {subsystems}
                '''
        indent = 4*' '
        tpl_import_prefix = 'from ..templates'
        templates_imports = '\n'.join(['%s import %s'%(tpl_import_prefix,i)
                                        for i in self.templates])
        
        subsystems = ['%s = %s.topology(%r)'%(subsys, template, subsys)\
                      for subsys, template in self.subsystems_templates.items()]
            
        subsystems = '\n'.join(subsystems)
        subsystems = textwrap.dedent(subsystems)
        subsystems = textwrap.indent(subsystems,indent).lstrip()
        text = text.expandtabs()
        text = textwrap.dedent(text)
        text = text.format(templates_imports = templates_imports,
                           subsystems = subsystems)
        return text

    def write_class_init(self):
        text = '''                
                class topology(num_assm):
                    
                    def __init__(self):
                        subsystems = {subsystems}
                        interface_map = {interface_map} 
                        indicies_map  = {indicies_map} 
                        super().__init__(subsystems, interface_map, indicies_map)
                    
                    def _map_coordinates(self):
                        pass
                    def _map_velocities(self):
                        pass
                    def _map_accelerations(self):
                        pass
               '''
        
        subsystems = ','.join(['subsystems.%s'%i for i in self.subsystems.keys()])
        interface_map = self.interface_map
        indicies_map  = self.nodes_indicies
        text = text.expandtabs()
        text = textwrap.dedent(text)
        text = text.format(subsystems = subsystems,
                           interface_map = interface_map,
                           indicies_map  = indicies_map)
        return text


    def write_constants_evaluator(self):
        text = '''
                def _map_constants(self):
                    {subsystems}
                    {virtuals_map}
                '''
        indent = 4*' '
        p = self.printer
        text = text.expandtabs()
        text = textwrap.dedent(text)
        
        subsystems = '\n'.join(['%s = subsystems.%s'%(i,i) for i in self.subsystems.keys()])
        subsystems = textwrap.dedent(subsystems)
        subsystems = textwrap.indent(subsystems,indent).lstrip()

        ground_map = self.mapped_gen_coordinates[0:2]
        pattern = '|'.join([p._print(i.lhs) for i in ground_map])

        virtuals_map = self.mapped_vir_coordinates
        pattern1 = '|'.join([p._print(i.lhs) for i in virtuals_map])
        pattern2 = '|'.join([p._print(i.rhs) for i in virtuals_map])
        
        def sub(x):
            l = x.group(0).split('.')
            try:
                s = '%s.config.%s'%(*l,)
            except TypeError:
                s = '%s'%x.group(0)
            return s
        self_inserter = self._insert_string('self.')
        
        virtuals_map = '\n'.join([p._print(expr) for expr in virtuals_map])
        virtuals_map = re.sub(pattern,self_inserter,virtuals_map)
        virtuals_map = re.sub(pattern1,sub,virtuals_map)
        virtuals_map = re.sub(pattern2,sub,virtuals_map)
        virtuals_map = textwrap.indent(virtuals_map,indent).lstrip()
        
        text = text.format(subsystems = subsystems ,
                           virtuals_map = virtuals_map)
        text = textwrap.indent(text,indent)
        return text
    
    def write_coordinates_setter(self):
        return self._write_x_setter('coordinates','q')
    
    def write_velocities_setter(self):
        return self._write_x_setter('velocities','qd')
    
    def write_accelerations_setter(self):
        return self._write_x_setter('accelerations','qdd')
    
    def _write_x_setter(self, func_name, var='q'):
        text = '''
                def _map_{func_name}(self,{var}):
                    {subsystems}
                    {virtuals_map}
               '''
        indent = 4*' '
        p = self.printer
        text = text.expandtabs()
        text = textwrap.dedent(text)
        
        self_inserter = self._insert_string('self.')
        
        ground_map = getattr(self,'mapped_gen_%s'%func_name)[0:2]
        pattern = '|'.join([p._print(i.lhs) for i in ground_map])
        ground_map = '\n'.join([p._print(i) for i in ground_map])
        ground_map = re.sub(pattern,self_inserter,ground_map)
        ground_map = textwrap.indent(ground_map,indent).lstrip()

        subsystems = '\n'.join(['%s = subsystems.%s'%(i,i) for i in self.subsystems.keys()])
        subsystems = textwrap.dedent(subsystems)
        subsystems = textwrap.indent(subsystems,indent).lstrip()

        virtuals_map = getattr(self,'mapped_vir_%s'%func_name)
        pattern1 = '|'.join([p._print(i.lhs) for i in virtuals_map])
        pattern2 = '|'.join([p._print(i.rhs) for i in virtuals_map])
        sub = self._insert_string('')
        virtuals_map = '\n'.join([str(p._print(i)) for i in virtuals_map])
        virtuals_map = re.sub(pattern,self_inserter,virtuals_map)
        virtuals_map = re.sub(pattern1,sub,virtuals_map)
        virtuals_map = re.sub(pattern2,sub,virtuals_map)
        virtuals_map = textwrap.indent(virtuals_map,indent).lstrip()
                
        text = text.format(func_name = func_name,
                           var = var,
                           ground_map = ground_map,
                           virtuals_map = virtuals_map,
                           subsystems = subsystems)
        text = textwrap.indent(text,indent)
        return text

    def write_code_file(self, dir_path=''):
        file_path = os.path.join(dir_path, self.name)
        imports = self.write_imports()
        system_class = self.write_system_class()
        text = ''.join([imports, system_class])
        with open('%s.py'%file_path, 'w') as file:
            file.write(text)
        print('File full path : %s.py'%file_path)
        
    def write_system_class(self):
        text = '''
                {class_init}
                    {constants}
                    {coord_setter}
                    {veloc_setter}
                    {accel_setter}
                '''
        text = text.expandtabs()
        text = textwrap.dedent(text)
        
        class_init = self.write_class_init()
        constants = self.write_constants_evaluator()
        coord_setter = self.write_coordinates_setter()
        veloc_setter = self.write_velocities_setter()
        accel_setter = self.write_accelerations_setter()
        lagrg_setter = self.write_lagrange_setter()
                
        text = text.format(class_init = class_init,
                           constants = constants,
                           coord_setter = coord_setter,
                           veloc_setter = veloc_setter,
                           accel_setter = accel_setter,
                           lagrg_setter = lagrg_setter)
        return text

