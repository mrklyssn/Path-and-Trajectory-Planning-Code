# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 16:00:34 2022

@author: Acer
"""

import numpy as np
import roboticstoolbox as rtb
from roboticstoolbox import DHRobot, RevoluteDH, ERobot, ELink, ETS, PrismaticDH

8
# link lengths in mm
a1 = float(input("a1 = ")) # For testing, 150 mm
a2 = float(input("a2 = ")) # For testing, 80 mm
a3 = float(input("a3 = ")) # For testing, 70 mm
a4 = float(input("a4 = ")) # For testing, 60 mm0

# link converted to meters
def mm_to_meter(a):
    m = 1000 # 1 meter = 1000 mm
    return a/m

a1 = mm_to_meter(a1)
a2 = mm_to_meter(a2)
a3 = mm_to_meter(a3)
a4 = mm_to_meter(a4)

# link limits converted to meters
d1 = float(input("d1 = ")) # 70mm
d1 = mm_to_meter(d1)

d2 = float(input("d2 = ")) # 60mm
d2 = mm_to_meter(d2)

d3 = float(input("d3 = ")) # 50mm
d3 = mm_to_meter(d3)

# Create Links
# [robot variable]=DHRobot([RevoluteDH(theta,r/a,alpha,offset)])
Carte_Standard = DHRobot([
    PrismaticDH(0,0,(270/180)*np.pi,a1,qlim=[0,0]),
    PrismaticDH((270/180)*np.pi,0,(270/180)*np.pi,a2,qlim=[0,d1]),
    PrismaticDH((270/180)*np.pi,0,(90/180)*np.pi,a3,qlim=[0,d2]),
    PrismaticDH(0,0,0,a4,qlim=[0,d3])],name= 'Cartesian')

print(Carte_Standard)

# degrees to radian convertion
def deg_to_rad(T):
    return (T/180.0)*np.pi

# q paths
q0 = np.array([0,0,0,0])

q1 = np.array ([0, 
                mm_to_meter(35),#float(input("d1 = "))),
                mm_to_meter(35),#float(input("d2 = "))),
                mm_to_meter(35)])#float(input("d3 = ")))])
    
q2 = np.array ([0, 
                mm_to_meter(35),#float(input("d1 = "))),
                mm_to_meter(35),#float(input("d2 = "))),
                mm_to_meter(0)])#float(input("d3 = ")))])

q3 = np.array ([0, 
                mm_to_meter(35),#float(input("d1 = "))),
                mm_to_meter(35),#float(input("d2 = "))),
                mm_to_meter(35)])#float(input("d3 = ")))])


q4 = np.array ([0, 
                mm_to_meter(35),#float(input("d1 = "))),
                mm_to_meter(35),#float(input("d2 = "))),
                mm_to_meter(0)])#float(input("d3 = ")))])

q5 = np.array ([0, 
                mm_to_meter(35),#float(input("d1 = "))),
                mm_to_meter(0),#float(input("d2 = "))),
                mm_to_meter(0)])#float(input("d3 = ")))])

q6 = np.array ([0, 
                mm_to_meter(35),#float(input("d1 = "))),
                mm_to_meter(0),#float(input("d2 = "))),
                mm_to_meter(35)])#float(input("d3 = ")))])

q7 = np.array ([0, 
                mm_to_meter(35),#float(input("d1 = "))),
                mm_to_meter(0),#float(input("d2 = "))),
                mm_to_meter(0)])#float(input("d3 = ")))])

q8 = np.array ([0, 
                mm_to_meter(0),#float(input("d1 = "))),
                mm_to_meter(0),#float(input("d2 = "))),
                mm_to_meter(0)])#float(input("d3 = ")))])
q9 = np.array ([0, 
                mm_to_meter(0),#float(input("d1 = "))),
                mm_to_meter(0),#float(input("d2 = "))),
                mm_to_meter(35)])#float(input("d3 = ")))])

q10 = np.array ([0, 
                mm_to_meter(0),#float(input("d1 = "))),
                mm_to_meter(0),#float(input("d2 = "))),
                mm_to_meter(0)])#float(input("d3 = ")))])

q11 = np.array ([0, 
                mm_to_meter(0),#float(input("d1 = "))),
                mm_to_meter(35),#float(input("d2 = "))),
                mm_to_meter(0)])#float(input("d3 = ")))])

q12 = np.array ([0, 
                mm_to_meter(0),#float(input("d1 = "))),
                mm_to_meter(35),#float(input("d2 = "))),
                mm_to_meter(35)])#float(input("d3 = ")))])

# Trajectory Commands
traj1 = rtb.jtraj(q0,q1,158)
print(traj1)
print (traj1.q)

print 
x1 = -0.2
x2 = 0.2
y1 = -0.2
y2 = 0.2
z1= -0.2
z2 = 0.2


#plot commands
#rtb.qplot(traj1.q)
Carte_Standard.plot(traj1.q,limits=[x1,x2,y1,y2,z1,z2],block=True)

Carte_Standard.teach(jointlabels=1)