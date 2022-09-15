#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 05:15:07 2020

@author: tikantsoi

Carry out 3D and 2D rendering
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
                
def render3d(sim, title, x1, x2, y1, y2):
    """
    Create a 3D plot of all the light rays
    """
    fig = plt.figure()
    ax=fig.add_subplot(111, projection='3d')
    ax.title.set_text(title)
        
    for ray in sim.rays():
        X = [point[0] for point in ray.vertices()]
        Y = [point[1] for point in ray.vertices()]
        Z = [point[2] for point in ray.vertices()]
        ax.plot3D(X,Y,Z)
        
    plt.grid() 
    plt.xlim(x1, x2)
    plt.ylim(y1, y2)
    ax.set_xlabel("x (mm)")
    ax.set_ylabel("y (mm)")
    ax.set_zlabel("z (mm)")
    plt.show()
    
def render2d(sim, title, x1, x2, y1, y2):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.title.set_text(title)
    
    for ray in sim.rays():
        X = [ray.p()[0]]
        Y = [ray.p()[1]]
        ax.scatter(X,Y)
    
    plt.grid()
    plt.xlim(x1, x2)
    plt.ylim(y1, y2)
    plt.xlabel("x (mm)")
    plt.ylabel("y (mm)")
    plt.show()
    
