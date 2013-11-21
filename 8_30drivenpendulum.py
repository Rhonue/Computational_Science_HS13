#Driven Pendulum
#Beat Lauber

import numpy as np
from scipy import *
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import random

w=-2
e=0.3

def pendulum(y,t):
    global w,e
    dx= y[1]     #dx/dt
    dy= -sin(y[0])-e*sin(y[0]-w*t)  #dy/dt
    return np.array([dx,dy])


time= np.linspace(0.0,100.0,1001)*2*pi/abs(w)
p1=[]
q1=[]

for i in range(50):
    p=random.uniform(-3.,3.)
    q=random.uniform(-pi,pi)
    yinit = np.array([q, p]) #initial values
    y = odeint(pendulum, yinit, time)
    for j in range(len(time)):
        if abs(time[j]-pi)<0.001:
            h=j
            break
       # else:
        #    h=-1
    print(h)
    for j in range(len(time)//h):
        q1+=[y[j*h,0]]
        p1+=[y[j*h,1]]
    
#y[:,0]=y[:,0]%(2*pi)
q1=np.array(q1)
p1=np.array(p1)
q1=q1%(2*pi)

for i in range(len(q1)):
    if q1[i] > pi:
        q1[i]-=2*pi


plt.figure()
plt.plot(q1,p1,'b.')
plt.title('Driven Pendulum')
plt.xlabel('q')
plt.ylabel('p')
plt.show()
     
''' for a=y and x=1, the popolation of both duck and fox remain constant'''
