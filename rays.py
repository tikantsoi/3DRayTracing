#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 16:54:38 2020

@author: tikantsoi

Provide sources of light rays, including Ray() and UniformCollimatedBeam().
"""

import numpy as np
import utils as ut
import simulation

class Ray:
    """
    Objects represent optical rays, they consist of a position, direction and frequency.
    The vertices attribute records the positions of the ray at the input plane and its subsequent incidence with other optical elements.
    """
    
    def __init__(self, p=np.zeros(3), k=ut.vec([0,0,1]), freq=float(1)):
        self.__vertices = [ut.vec(p)]
        self.__p = ut.vec(p)
        self.__k = ut.vec(k)
        self.__freq = float(freq)
        self.terminated = False   
        
    def vertices(self):
        return self.__vertices
        
    def p(self):
        return self.__vertices[-1]
    
    def k(self):
        return self.__k
    
    def freq(self):
        return self.__freq
    
    def khat(self):
        """
        Provide the unit vector for the direction
        """
        return ut.hat(self.__k)
    
    def append(self, newp):
        """
        Add new positions to the ray along its path
        """
        if len(newp) != 3 or not isinstance(newp, np.ndarray):
            raise TypeError
        self.__vertices.append(ut.vec(newp))
        
    def ksetter(self, newk):
        """
        Set a new direction
        """
y        if len(newk) != 3 or not isinstance(newk, np.ndarray):
           raise TypeError
        self.__k = ut.vec(newk)
    
    def __repr__(self):
        return "%s(p=%s, k=%s, vertices=%s, freq=%g)" % ("Ray", self.__vertices[-1], self.__k, self.__vertices, self.__freq)
    
class UniformCollimatedBeam:
    """
    Create light rays in rings from a circular surface.
    The rays are arranged to have a near uniform density distribution across the surface.
    """

    def __init__(self, centre=np.zeros(3), k=ut.vec([0,0,1]), radius=2.5, density=0.625): 
        self.__points = []
        self.__objectlist = []
        self.__centre = ut.vec(centre)
        self.__k = ut.vec(k)
        self.__radius = float(radius)
        self.__density = float(density)
        
    def points(self):
        """
        Points given in vector form.
        """
        return self.__points
    
    def objectlist(self):
        """
        Stored as Ray() objects, used in simulation.
        """
        return self.__objectlist

    def generate(self):
        """
        Points are created along an axis in a fixed interval.
        Rings of points are then created by rotating the points on the axis, starting from the inner most circle.
        """
        axis = np.arange(0, self.__radius + self.__density, self.__density).tolist()
        for point in axis:
            axialpoint = ut.vec([point,0,0]) + self.__centre
            self.__points.append(axialpoint)
        for point in axis[1:]:
            N = 3 * (2 ** (axis.index(point)))
            angle = 2 * np.pi / N
            r = point
            for k in range(N-1):
                x = r * np.cos(angle * (k+1))
                y = r * np.sin(angle * (k+1))
                newpoint = ut.vec([x,y,0]) + self.__centre
                self.__points.append(newpoint)
        for point in self.__points: #Turning every item in the list to a Ray()
            self.__objectlist.append(Ray(point, self.__k))
    
    def rms(self, sim):
        """
        Calculate the RMS spot radius.
        """
        total = 0
        for ray in sim.rays():
            squareddiff = ut.norm(ut.vec([ray.p()[0] - sim.rays()[0].p()[0], ray.p()[1] - sim.rays()[0].p()[1], 0])) * ut.norm(ut.vec([ray.p()[0] - sim.rays()[0].p()[0], ray.p()[1] - sim.rays()[0].p()[1], 0]))
            total = total + squareddiff
        rms = np.sqrt(total / (len(sim.rays()))) 
        return rms
   
   


            
            
        
    
    
