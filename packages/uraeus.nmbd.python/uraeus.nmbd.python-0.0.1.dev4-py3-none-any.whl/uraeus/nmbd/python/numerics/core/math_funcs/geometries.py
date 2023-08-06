#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 18:52:02 2019

@author: khaledghobashy
"""

# Standard library imports.
from collections import namedtuple

# Third party imports.
import numpy as np

# Local imports.
from .spatial_alg import triad, centered, oriented
from .numba_funcs import A, dcm2ep


geometry = namedtuple('geometry', ['R','P','m','J'])

def cylinder_geometry(arg1, arg2, ro=10, ri=0):
    v = arg2 - arg1
    l = np.linalg.norm(v)
    frame = triad(v)
    
    density = 7.9*1e-3
    vol = np.pi*(ro**2-ri**2)*l
    m   = density*vol
    Jzz = (m/2)*(ro**2+ri**2)
    Jxx = Jyy = (m/12)*(3*(ro**2+ri**2)+(l**2))
    
    
    R = centered(arg1,arg2)
    P = dcm2ep(frame)
    J = np.diag([Jxx,Jyy,Jzz])
    
    J = A(P).dot(J).dot(A(P).T) # chamged from A(P).dot(J).dot(A(P).T)
    P = np.array([[1],[0],[0],[0]],dtype=np.float64)
    
    return geometry(R,P,m,J)


def triangular_prism(p1,p2,p3,thickness=10):
    v1 = p1-p2
    v2 = p1-p3
    v3 = p2-p3
    
    l1 = np.linalg.norm(v1) # assuming this is the base, where p3 is the vertix
    l2 = np.linalg.norm(v2)
    l3 = np.linalg.norm(v3)
    pr = (l1+l2+l3)/2 # half the premiter
    
    # The normal height of the vertix from the base.
    theta = np.arccos((v1.T.dot(v2))/(l1*l2))
    height = l2*np.sin(theta)
    area   = np.sqrt(pr*(pr-l1)*(pr-l2)*(pr-l3))
    volume = area*thickness
    density = 7.8*1e-3 #(gm/mm3)
            
    # Creating a centroidal reference frame with z-axis normal to triangle
    # plane and x-axis oriented with the selected base vector v1.
    n = oriented(p1,p2,p3)
    frame = triad(n,v1)
    
    # Calculating the principle inertia properties "moment of areas" at the
    # geometry centroid.
    a   = v2.T.dot(v1/l1) # Offset of p3 from p1 projected on v1.
    Ixc = (l1*height**3)/36
    Iyc = ((l1**3*height)-(l1**2*height*a)+(l1*height*a**2))/36
    Izc = ((l1**3*height)-(l1**2*height*a)+(l1*height*a**2)+(l1*height**3))/36
    
    # Evaluating the moments of inertia of the side-walls
    Ix_n = (1/12) * thickness**3 * l1
    Iy_n = (1/12) * thickness**3 * height
        
    # Evaluating mass
    m = density*volume
    
    # Calculating the total moment of inertia from the moment of areas
    Ix = ((m/area) * float(Ixc)) + ((m/(thickness*l1))*Ix_n)
    Iy = ((m/area) * float(Iyc)) + ((m/(thickness*height))*Iy_n)
    Iz = (m/area) * float(Izc)

    # Evaluate Geometry properties
    J = np.diag([float(i) for i in [Ix, Iy, Iz]])
    R = centered(p1,p2,p3)
    P = dcm2ep(frame)

    # Transforming Inertia to the Global Frame
    J = A(P).dot(J).dot(A(P).T)
    P = np.array([[1],[0],[0],[0]],dtype=np.float64)
    
    return geometry(R,P,m,J)


def sphere_geometry(point, raduis):
    
    vol = np.pi*(4/3) * raduis**3 * 1e-3
    m   = 7.9*vol
    Jp  = (2/5) * m * raduis**2
    
    R = point
    J = np.diag([Jp, Jp, Jp])
    P = np.array([[1],[0],[0],[0]],dtype=np.float64)
    
    return geometry(R, P, m, J)


def composite_geometry(*geometries):
    
    # composite body total mass as the sum of it's subcomponents
    m = sum([i.m for i in geometries])
    # center of mass vector relative to the origin
    R = (1/m) * sum([g.m*g.R for g in geometries])
    
    J = sum([ A(g.P).dot(g.J).dot(A(g.P).T) 
            + g.m*(np.linalg.norm(g.R-R)**2*np.eye(3)-(g.R-R).dot((g.R-R).T)) 
            for g in geometries])
    
    P = np.array([[1],[0],[0],[0]],dtype=np.float64)
    
    return geometry(R,P,m,J)

###############################################################################
