#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 12:32:28 2020

@author: tikantsoi

Record all the testings
"""

import rays
import opticalelements
import simulation
import graphics
import numpy as np

#%% create objects

r_task2 = rays.Ray()

#%% Task 2
"""
Test the methods of Ray()
"""

r_task2.p()
#array([0., 0., 0.])

r_task2.k()
#array([0, 0, 1])

r_task2.freq()
#1.0

"""
Set a new k
"""
r_task2.ksetter([0,0,2])
r_task2.k()
#array([0., 0., 2.])

r_task2.khat()
#array([0., 0., 1.])

r_task2.vertices() 
#[array([0., 0., 0.])]

r_task2.append([0,0,3])
r_task2.p()
#array([0., 0., 3.])
r_task2.vertices()
#[array([0., 0., 0.]), array([0., 0., 3.])]

r_task2
#Ray(p=[0. 0. 3.], k=[0. 0. 2.], vertices=[array([0., 0., 0.]), array([0., 0., 3.])])

#%% create objects

o_task3 = opticalelements.OpticalElements([0,0,1])

s_task3 = opticalelements.SphericalRefraction(0.2,0.15,[0,0,1])

#%% task 3
"""
Test the methods of OpticalElements()
"""

o_task3.pos()
#array([0., 0., 1.])

o_task3.n1()
#1.0

o_task3.n2()
#1.5

o_task3
#OpticalElements(pos=[0. 0. 1.], n1=1, n2=1.5)

"""
Test the methods of SphericalRefraction()
"""

s_task3
#SphericalRefraction(curv=0.2, curvrad=5, aperad=0.15, n1=1, n2=1.5, pos=[0. 0. 1.], centre=[0. 0. 6.])
#%% create objects

s_task4 = opticalelements.SphericalRefraction(0.2,0.15,[0,0,1])

r_task4 = rays.Ray()

s_neg_task4 = opticalelements.SphericalRefraction(-0.2,0.15,[0,0,10])

r_neg_task4 = rays.Ray()

r_x1_task4 = rays.Ray([1,0,0])

#%% task 4
"""
Test the intercept() method
"""
s_task4.intercept(r_task4)
#1.0

"""
Try negative curvature
"""
s_neg_task4.intercept(r_neg_task4) 
#10.0

"""
At some height x=1 for both surfaces
"""
s_task4.intercept(r_x1_task4)
#1.1010205144336433, greater than 1 

s_neg_task4.intercept(r_x1_task4)
#9.898979485566358 less than 10

#%% create objects

s_task5 = opticalelements.SphericalRefraction(0.2,0.15,[0,0,1])

r_task5 = rays.Ray()

r_y1_task5 = rays.Ray([0,1,0],[0,-1,1])

r_minusy1_task5 = rays.Ray([0,-1,0],[0,1,1])

s_tir_task5 = opticalelements.SphericalRefraction(0.2,0.15,[0,0,1],0.15,0.1)

r_tir_task5 = rays.Ray([0,1,0],[0,-1,1])

#%% task 5
"""
Test the refraction() method
"""

s_task5.refraction(r_task5)

r_task5
#Ray(p=[0. 0. 1.], k=[0. 0. 1.], vertices=[array([0., 0., 0.]), array([0., 0., 1.]), array([0., 0., 1.])], freq=1)

"""
Incident angle of 45 degrees
"""
s_task5.refraction(r_y1_task5)

r_y1_task5
#Ray(p=[0.00000000e+00 7.77156117e-16 1.00000000e+00], k=[ 0.         -0.47140452  0.8819171 ], vertices=[array([0., 1., 0.]), array([0.00000000e+00, 7.77156117e-16, 1.00000000e+00])], freq=1)
#-0.47140452 / 0.8819171 = -0.53452
#refracted angle = 28.1 degrees

s_task5.refraction(r_minusy1_task5)

r_minusy1_task5
#Ray(p=[ 0.00000000e+00 -7.77156117e-16  1.00000000e+00], k=[0.         0.47140452 0.8819171 ], vertices=[array([ 0., -1.,  0.]), array([ 0.00000000e+00, -7.77156117e-16,  1.00000000e+00])], freq=1)
#0.47140452 / 0.8819171 = 0.53452
#same refracted angle

"""
total internal reflection
"""
s_tir_task5.refraction(r_tir_task5)

r_tir_task5
#None

#%% create objects

s_task7 = opticalelements.SphericalRefraction(0.2,0.15,[0,0,1])

r_task7 = rays.Ray([0,1,0])

r_y100_task7 = rays.Ray([0,100,0])

r_y1_task7 = rays.Ray([0,1,0],[1,1,0])

r_x1_task7 = rays.Ray([1,0,0],[1,1,1])

#%% task 7
"""
Propagate rays
"""
s_task7.propagate_ray(r_task7)

r_task7
#Ray(p=[0.         1.         1.10102051], k=[ 0.         -0.06607142  0.99034918], vertices=[array([0., 1., 0.]), array([0.        , 1.        , 1.10102051])], freq=1)
#Successfully propagated

"""
Test the case where the ray does not intercept with the surface
"""
s_task7.propagate_ray(r_y100_task7)

r_y100_task7
#Ray is terminated

"""
A range of rays
"""
s_task7.propagate_ray(r_y1_task7)

r_y1_task7
#Terminated, propagating in x-y plane so no intercept

s_task7.propagate_ray(r_x1_task7)

r_x1_task7
#Terminated, outside of the refracting surface
#%% create objects

o_task8 = opticalelements.OutputPlane()

r_task8 = rays.Ray()

#%% task 8
"""
Test propgating rays with OutputPlane()
"""
o_task8.intercept(r_task8)
#10.0

o_task8.propagate_ray(r_task8)
#10.0

r_task8
#Ray(p=[ 0.  0. 10.], k=[0. 0. 1.], vertices=[array([0., 0., 0.]), array([ 0.,  0., 10.])], freq=1)

#%% create objects

sim_task9 = simulation.Simulation()

r_y1_task9 = rays.Ray([0,1,0])

r_y2_task9 = rays.Ray([0,2,0])

r_y3_task9 = rays.Ray([0,3,0])

r_x1_task9 = rays.Ray([1,0,0])

r_x2_task9 = rays.Ray([2,0,0])

r_x3_task9 = rays.Ray([3,0,0])

s_task9 = opticalelements.SphericalRefraction(0.03, 1/0.03, [0,0,100])

o_task9 = opticalelements.OutputPlane([0,0,250]) 

#%% task 9
"""
Test the simulation process
First add the optical elements to the system
Then propagate the rays 
"""
sim_task9.appendelements(s_task9,o_task9)
sim_task9.propagate([r_y1_task9,r_y2_task9,r_y3_task9,r_x1_task9,r_x2_task9,r_x3_task9])

sim_task9

graphics.render3d(sim_task9, "Task 9", -3, 3, -3, 3)

#%% create objects

sim_task10 = simulation.Simulation()

r1_task10 = rays.Ray([0,0.1,0])

r2_task10 = rays.Ray([0,5,0])

r3_task10 = rays.Ray([0,10,0])

r4_task10 = rays.Ray([0,15,0])

r5_task10 = rays.Ray([0,20,0])

s_task10 = opticalelements.SphericalRefraction(0.03, 1/0.03, [0,0,100])

o_task10 = opticalelements.OutputPlane([0,0,250]) 

#%% task 10
"""
Calculating the paraxial focus using simple geometry
"""
sim_task10.appendelements(s_task10,o_task10)
sim_task10.propagate([r1_task10,r2_task10,r3_task10,r4_task10,r5_task10])

graphics.render3d(sim_task10, "Task 10", -20,20,-20,20)

theta = abs(r1_task10.k()[1] / r1_task10.k()[2])

print(theta)
#0.001000000166666071

paraxialfocus = (r1_task10.vertices()[1][2] + r1_task10.vertices()[0][1] / theta)
print(paraxialfocus)
#200.00013333373323

#%% create objects

sim_task11 = simulation.Simulation()

r_task11 = rays.Ray()

r1_task11 = rays.Ray([1,0,0])

r9_task11 = rays.Ray([10,0,0])

r2_task11 = rays.Ray([-1,0,0])

r3_task11 = rays.Ray([0,1,0])

r4_task11 = rays.Ray([0,-1,0])

r5_task11 = rays.Ray([1,1,0])

r6_task11 = rays.Ray([1,-1,0])

r7_task11 = rays.Ray([-1,1,0])

r8_task11 = rays.Ray([-1,-1,0])

s_task11 = opticalelements.SphericalRefraction(0.03, 1/0.03, [0,0,100])

o_task11 = opticalelements.OutputPlane([0,0,-10]) 

#%% task 11
"""
To test the spherical surface
Try reflecting off the surface
Would require to switch off the propagate_ray method containing refraction
"""
s_task11.intercept(r_task11)

s_task11.reflection(r_task11)

r_task11
#Ray(p=[  0.   0. 100.], k=[ 0.  0. -1.], vertices=[array([0., 0., 0.]), array([  0.,   0., 100.])], freq=1)
#reflected

sim_task11.appendelements(s_task11,o_task11)
sim_task11.propagate([r_task11, r1_task11, r2_task11, r3_task11, r4_task11, r5_task11, r6_task11, r7_task11, r8_task11])

graphics.render3d(sim_task11, "Task 11", -10, 10, -10, 10)

sim_task11

#%% create objects

sim_task12 = simulation.Simulation()

b_task12 = rays.UniformCollimatedBeam() 

s_task12 = opticalelements.SphericalRefraction(0.03, 1/0.03, [0,0,100])

o_task12 = opticalelements.OutputPlane([0,0,200.00013333373323]) 

#%% task 12
"""
Test UniformCollimatedBeam()
First generate the rays
Then propagate
"""
b_task12.generate()

sim_task12.appendelements(s_task12, o_task12)

sim_task12.propagate(b_task12.objectlist())

graphics.render3d(sim_task12, "Task 12", -2.5, 2.5, -2.5, 2.5)

#%% task 13
"""
2D rendering to produce the spot diagram
"""
graphics.render2d(sim_task12, "Task 13", -0.002, 0.002, -0.002, 0.002)
 
"""
RMS spot radius
"""
b_task12.rms(sim_task12)
#0.0009884228132171987 mm

distance = 250 - 100

alpha = np.arctan(b_task12.rms(sim_task12)/ distance)

print(2*alpha)
#1.3178970842705234e-05 rad
#%% task 14
"""
Diffraction limit = 1.22 * lambda * focal length / aberture diameter
"""
dlim = 1.22 * (1/3e8) * 200.00013333373323 / 5 #wavelength so small number doesnt matter

print(dlim)
#1.6266677511143636e-07 factor of 2 out

#%% create objects

sim_task15 = simulation.Simulation()

r_task15 = rays.Ray([0,0.1,0])

s_task15 = opticalelements.SphericalRefraction(0.02, 1/0.02, [0,0,100], 1, 1.5168)

p_task15 = opticalelements.Plane([0,0,105], 1.5168)

o_task15 =  opticalelements.OutputPlane([0,0,250])

b_task15 = rays.UniformCollimatedBeam(np.zeros(3), np.array([0,0,1]), 5, 1.25)

sim_part1_task15 = simulation.Simulation()

o_part1_task15 = opticalelements.OutputPlane([0,0,245.12392329876656])

#%% task 15 part 1
"""
Model a plano-convex lens with a spherical refracting surface and a plane
Results are recorded on the output surface
"""
sim_task15.appendelements(s_task15, p_task15, o_task15)

sim_task15.propagate([r_task15])

theta = abs(r_task15.k()[1] / r_task15.k()[2])

print(theta) 
#0.0006890667412627269

paraxialfocus = (r_task15.vertices()[1][2] + r_task15.vertices()[0][1] / theta)
print(paraxialfocus)
#245.12392329876656 

b_task15.generate()

sim_part1_task15.appendelements(s_task15, p_task15, o_part1_task15)

sim_part1_task15.propagate(b_task15.objectlist())

graphics.render3d(sim_part1_task15, "Task 15.1", -5, 5, -5, 5)

graphics.render2d(sim_part1_task15, "Task 15.2", -0.01, 0.01, -0.01, 0.01)

"""
RMS spot radius
"""
b_task15.rms(sim_part1_task15)
#0.005501345612560001

#%% create objects

simm_task15 = simulation.Simulation()

rr_task15 = rays.Ray([0,0.1,0])

ss_task15 = opticalelements.SphericalRefraction(0.02, 1/0.02, [0,0,105], 1, 1.5168)

pp_task15 = opticalelements.Plane([0,0,100], 1.5168)

oo_task15 =  opticalelements.OutputPlane([0,0,250])

bb_task15 = rays.UniformCollimatedBeam(np.zeros(3), np.array([0,0,1]), 5, 1.25)

simm_part2_task15 = simulation.Simulation()

oo_part2_task15 = opticalelements.OutputPlane([0,0,250.12392329876644])

#%% task 15 part 2

simm_task15.appendelements(ss_task15, pp_task15, oo_task15)

simm_task15.propagate([rr_task15])

thetaa = abs(rr_task15.k()[1] / rr_task15.k()[2])

print(thetaa) 
#0.0006890667412627279

paraxialfocuss = (rr_task15.vertices()[1][2] + rr_task15.vertices()[0][1] / thetaa)
print(paraxialfocuss)
#250.12392329876644 

bb_task15.generate()

simm_part2_task15.appendelements(ss_task15, pp_task15, oo_part2_task15)

simm_part2_task15.propagate(bb_task15.objectlist())

graphics.render3d(simm_part2_task15, "Task 15.3", -5, 5, -5, 5)

graphics.render2d(simm_part2_task15, "Task 15.4", -0.01, 0.01, -0.01, 0.01)

"""
RMS spot radius
"""
bb_task15.rms(simm_part2_task15)
#0.005610358498606609
