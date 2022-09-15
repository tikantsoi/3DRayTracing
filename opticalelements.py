#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 17:41:18 2020

@author: tikantsoi

Contain objects that are able to reflect / refract and detect light rays.
"""

import numpy as np
import utils as ut
import rays
    
class OpticalElements:
    """
    Base class for all optical elements.
    """
    
    def __init__(self, pos=ut.vec([0,0,10]), n1=float(1), n2=float(1.5)):
        self.__pos = ut.vec(pos)
        self.__n1 = float(n1)
        self.__n2 = float(n2)
        
    def pos(self):
            return self.__pos
        
    def n1(self):
            return self.__n1
        
    def n2(self):
            return self.__n2
    
    def propagate_ray(self, ray):
        "propagate a ray through the optical element"
        raise NotImplementedError()
        
    def __repr__(self):
         return "%s(pos=%s, n1=%g, n2=%g)" % ("OpticalElements", self.__pos, self.__n1, self.__n2)
        
         
class SphericalRefraction(OpticalElements):
    """
    Create spherical refracting surfaces.
    The surface is described by 5 parameters:
        
    - the intercept with the z axis

    - the curvature 

    - n1, n2 refractive indices either side of the surface

    - the aperture radius 
    """

    def __init__(self, curv, aperad, *args):
        super().__init__(*args)
        self.__curv = float(curv)
        if self.__curv == 0:
            raise ValueError("Curvature of the surface is zero.")
        self.__curvrad = 1/ self.__curv
        self.__aperad = float(aperad)
        self.__centre = self.pos() + ut.vec([0,0,self.__curvrad])
    
    def intercept(self, ray):
        """
        Return the valid intercept of the light ray with the surface, note the intercept can take either positive or negative values.
        """
        r = ray.p() - self.__centre
        rdotkhat = r.dot(ray.khat())
        insidesqrt = rdotkhat * rdotkhat - (ut.norm(r) * ut.norm(r) - self.__curvrad * self.__curvrad)
        if insidesqrt < 0:
            None#no valid intercept
            return ray.terminated
        sqrt = np.sqrt(insidesqrt)
        l_1 = - rdotkhat + sqrt
        l_2 = - rdotkhat - sqrt
        #d_aperad = ut.norm(ut.vec([0,self.__aperad,0]) + self.pos() - ray.p()) #distance from the position of the ray to the aperture radius
    
        if abs(rdotkhat) > 0: 
            if self.__curvrad > 0:
                intercept = min(l_1, l_2)
                #if intercept < d_aperad:
                return intercept
            else:
                intercept = max(l_1, l_2)
                #if intercept > d_aperad:
                return intercept
        else: #rdotkhat = 0
            intercept = l_1 #orthogonal so no only one intercept
            return intercept
            
    def refraction(self, ray):
        """
        Calculate the ray refraction by using the most general Snell's law in vector form.
        """
        if self.intercept(ray) == None:
           return ray.terminated
        else:
            pass
        
        newp = ray.p() + self.intercept(ray) * ray.khat() 
        ray.append(newp)
        
        if self.__curvrad > 0:
            normal = ut.hat(self.__centre - newp) 
        else:
            normal = - ut.hat(self.__centre - newp)
       
        normaldotkhat =  normal.dot(ray.khat())
        sintheta_1 = np.sqrt(1 - normaldotkhat * normaldotkhat)
        
        if sintheta_1 > self.n2() / self.n1(): #total internal reflection
            return None
        
        normaldotnewkhat = np.sqrt(1 - (self.n1() / self.n2() * sintheta_1) ** 2)
        newkhat = (self.n1() * ray.khat() + (self.n2() * normaldotnewkhat - self.n1() * normaldotnewkhat) * normal) / self.n2() 
        ray.ksetter(newkhat)
        
    def reflection(self, ray):
        """
        Calculate the ray reflection
        """
        if self.intercept(ray) == None:
           return ray.terminated
        else:
            pass
        
        newp = ray.p() + self.intercept(ray) * ray.khat() 
        ray.append(newp)
        
        if self.__curvrad > 0:
            normal = ut.hat(self.__centre - newp) 
        else:
            normal = - ut.hat(self.__centre - newp)
       
        normaldotkhat =  normal.dot(ray.khat())
        newkhat = ray.khat() - 2 * normaldotkhat * normal
        ray.ksetter(newkhat)
        
        
    def propagate_ray(self, ray):
        self.intercept(ray)
        self.refraction(ray)
        
        
        """
    def propagate_ray(self, ray): # Use only when studying reflection of rays
        self.intercept(ray)
        self.reflection(ray)
        """
        
    def __repr__(self):
        return "%s(curv=%g, curvrad=%g, aperad=%g, n1=%g, n2=%g, pos=%s, centre=%s)" % ("SphericalRefraction", self.__curv, self.__curvrad, self.__aperad, self.n1(), self.n2(), self.pos(), self.__centre)
    
class Plane(OpticalElements):
    """
    A refracting planar surface.
    The surface has a unit normal vector, as well as dimensions which are given in vectors.
    """
    def __init__(self, *args, normal=ut.vec([0,0,1]), width=ut.vec([2.5,0,0]), height=ut.vec([0,2.5,0])):
        super().__init__(*args)
        self.__normal = ut.vec(normal)
        self.__width = ut.vec(width)
        self.__height = ut.vec(height)
        if not width.dot(height) == 0: 
            raise ValueError("Not an orthogonal plane.")
            
    def normal(self):
        return self.__normal
    
    def width(self):
        return self.__width
    
    def height(self):
        return self.__height
        
    def intercept(self, ray):    
        normaldotkhat = self.__normal.dot(ray.khat())
        if abs(normaldotkhat) > 0:
            intercept = ut.norm((self.pos() - ray.p()) / normaldotkhat)
            newp = ray.p() + intercept * ray.khat()
            ray.append(newp)
            return intercept
        else:
            return None
        
        if intercept == None:
            return ray.terminated
        
    def refraction(self, ray): 
        normaldotkhat = self.__normal.dot(ray.khat())
        sintheta_1 = np.sqrt(1 - normaldotkhat * normaldotkhat)
        
        if sintheta_1 > self.n2() / self.n1(): #total internal reflection
            return None
        
        normaldotnewkhat = np.sqrt(1 - (self.n1() / self.n2() * sintheta_1) ** 2)
        newkhat = (self.n1() * ray.khat() + (self.n2() * normaldotnewkhat - self.n1() * normaldotnewkhat) * self.__normal) / self.n2() 
        ray.ksetter(newkhat)
    
    def propagate_ray(self, ray):
        self.intercept(ray)
        self.refraction(ray)
        
    def __repr__(self):
        return "%s(normal=%s, width=%s, height=%s, n1=%g, n2=%g, pos=%s,)" % ("Plane", self.__normal, self.__width, self.__height, self.n1(), self.n2(), self.pos())
        
class OutputPlane(Plane):
    """
    A plane where the light rays land.
    No reflection / refraction.
    """
    def __init__(self, *args):
        super().__init__(*args)
        
    def refraction(self, ray):
        raise NotImplementedError()
        
    def propagate_ray(self, ray):
        return self.intercept(ray)
        
    def __repr__(self):
        return "%s(normal=%s, width=%s, height=%s, n1=%g, n2=%g, pos=%s,)" % ("OutputPlane", self.normal(), self.width(), self.height(), self.n1(), self.n2(), self.pos())

                

    
    
        
     
            
        
            
    
            
        
    
   