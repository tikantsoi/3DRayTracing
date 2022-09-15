#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 04:58:11 2020

@author: tikantsoi

Contain light sources and optical elements.
Act as a simulator for raytracing.
"""

import rays
import opticalelements

class Simulation:
    def __init__(self):
        self.__elements = []
        self.__rays = []
    
    def elements(self):
        return self.__elements
    
    def rays(self):
        return self.__rays
    
    def appendelements(self, *elements):
        """
        Append optical elements to the system
        """
        for elem in elements:
            #if isinstance(elem, opticalelements.OpticalElements()):
            self.__elements.append(elem)
        #else:
            #raise TypeError   
    
    def propagate(self, objectlist):
        """
        Append a bundle of Ray() objects to the system and then propagate
        """
        
        for point in objectlist:
            #if isinstance(point, rays.Ray()):
            self.__rays.append(point)
            for elem in self.__elements:
                elem.propagate_ray(point)
        #else:
            #raise TypeError
                
    def __repr__(self):
        return "%s(elements=%s, rays=%s)" % ("Simulation", self.__elements, self.__rays)
        

       
  