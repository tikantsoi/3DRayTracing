#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 16:54:38 2020

@author: tikantsoi

Provide sources of light rays, including Ray() and UniformCollimatedBeam().
"""

import numpy as np
import utils as ut

class Ray:
    
    """
    Objects represent optical rays, they consist of a position, direction and frequency.
    The vertices attribute records the positions of the ray at the input plane and its subsequent incidence with other optical elements.
    """
    
    def __init__(self, p=np.zeros(3), k=ut.vec(0,0,1), frequency=1):
        self.__vertices = [ut.vec(p)]
        self.__p = np.array(p)
        self.__k = np.array(k)
        self.__frequency = frequency
        self.terminated = False
        
    def p(self):
        return self.__vertices[-1]
    
    def k(self):
        return self.__k
    
    def khat(self):
        return self.__k / np.linalg.norm(self.__k)
    
    def append(self, newp):
        if len(newp) != 3:
            raise TypeError
        self.__vertices.append(np.array(newp))
        
    def ksetter(self, newk):
        self.__k = np.array(newk)
    
    def vertices(self):
        return self.__vertices
    
class UniformCollimatedBeam:
   """
   unifrom collimated beam
   """

   def __init__(self, centre = np.zeros(3), k=np.array([0,0,1]), radius=2.5, density=0.5): #4 dots in first ring
        self.__points = []
        self.__centre = np.array(centre)
        self.__k = np.array(k)
        self.__radius = radius
        self.__density = density
    
   def reset(self):
       self.__points = []
   
   def points(self):
       return self.__points
   
   def radius(self):
       return self.__radius
   
   def centre(self):
       return self.__centre
    
   def k(self):
       return self.__k

   def generate(self):
        axis = [self.__centre]
        self.__points.append(Ray(self.__centre, self.__k))
        initialpoints = np.arange(self.__density,self.__radius+self.__density,self.__density).tolist()
        for i in initialpoints:
            point = np.array([i+self.__centre[0],0,0])
            axis.append(point)
            self.__points.append(Ray(point, self.__k))
        for j in axis[1:]:
            N = 6 * (2 ** (initialpoints.index(j[0])))
            angle = 2 * np.pi / N
            r = j[0] - self.__centre[0]
            for k in range(N-1):
                x = r * np.cos(angle * (k+1))
                y = r * np.sin(angle * (k+1))
                newpoint = np.array([x+self.__centre[0],y+self.__centre[1],self.__centre[2]])
                self.__points.append(Ray(newpoint, self.__k))
    
   def rms(self, sim):
       total = 0
       for elem in sim.rays():
           diffsquared = (np.linalg.norm(elem.p() - sim.rays()[0].p())) ** 2 # only works after generate and appendrays, to solve because not yet propagated ray so this will return 0,0,0 
           total = total + diffsquared
       rms = np.sqrt(total / (len(sim.rays()))) #only works after reset, manually set to 3 need to fix bug
       return rms
   
   


            
            
        
    
    
