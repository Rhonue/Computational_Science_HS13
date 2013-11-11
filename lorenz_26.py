#lorenz equations
"""
Created on Wed Nov  6 15:52:13 2013

@author: ruettir
"""

#runge kutta for chebyshev
"""
Created on Wed Nov  6 12:58:34 2013

@author: ruettir
"""
from math import cos, sin, pi
import numpy as np
import scipy
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tkinter import *
import random

#import Tkinter as tik
#import tkMessageBox

def lorenz(X,Y,Z,s,r,b):
    '''s=sigma, r=r, b=b'''
    T0=s*(Y-X)
    T1=r*X-Y-X*Z
    T2=X*Y-b*Z

    return np.array([T0,T1,T2])


def rk4(lorenz,t0,X0,Y0,Z0,s,r,b,dt):
    
    x0i=[X0]
    y0i=[Y0]
    z0i=[Z0]
    t0i=[t0]
    mmax=6000
    for m in range(1,mmax,1):
        xn=x0i[m-1]
        yn=y0i[m-1]
        zn=z0i[m-1]
        tn=t0i[m-1]
        
        dt1=dt*lorenz(xn,yn,zn,s,r,b)
        dt1x=dt1[0]
        dt1y=dt1[1]
        dt1z=dt1[2]
    
        dt2=dt*lorenz(xn+dt1x/2.0, yn+dt1y/2.0, zn+dt1z/2.0,s,r,b)
        dt2x=dt2[0]
        dt2y=dt2[1]
        dt2z=dt2[2]
        
        dt3=dt*lorenz(xn+dt2x/2.0, yn+dt2y/2.0, zn+dt2z/2.0,s,r,b)
        dt3x=dt3[0]
        dt3y=dt3[1]
        dt3z=dt3[2]
    
        dt4=dt*lorenz(xn+dt3x, yn+dt3y, zn+dt3z,s,r,b)
        dt4x=dt4[0]
        dt4y=dt4[1]
        dt4z=dt4[2]
    
        t0i+=[tn+dt]
        x0i+=[xn+(1.0/6)*(dt1x+2.0*dt2x+2.0*dt3x+dt4x)]
        y0i+=[yn+(1.0/6)*(dt1y+2.0*dt2y+2.0*dt3y+dt4y)]
        z0i+=[zn+(1.0/6)*(dt1z+2.0*dt2z+2.0*dt3z+dt4z)]
        
    return [t0i,x0i,y0i,z0i]

if __name__ == '__main__' :
    
    dt=0.01
    [s,r,b] = [10, 28, 8./3.]
    [t0, X0, Y0, Z0] = [0, 1, 1, 1]

    [t,XX,YY,ZZ] = rk4(lorenz, t0, X0, Y0, Z0, s, r, b,dt)


def ode(ht,wd,color):
    scalex=random.uniform(10.,100.)
    scaley=random.uniform(10.,100.)
    global XX, YY
    for i in range(len(XX)-1):
        x0=XX[i]
        x1=XX[i+1]
        y0=YY[i]
        y1=YY[i+1]
        #scale the points
        x0=x0*scalex+wd/2
        y0=y0*scaley+ht/2
        x1=x1*scalex+wd/2
        y1=y1*scaley+ht/2
        canv.create_line(x0, y0, x1, y1,fill=color)
        canv.update()


def screenSaver(wd,ht):
    """Create a screen saver
    @param wd with of the screen
    @param ht height of the screen
    """
    col=["red","green","blue","brown","gold","maroon"]
    while(1):
        for i in range(len(col)):
            canv.delete(ALL)
            ode(ht,wd,col[i])


screen=Tk()
wd, ht=screen.winfo_screenwidth(), screen.winfo_screenheight()
screen.overrideredirect(1)
screen.geometry("%dx%d+0+0"%(wd,ht))
canv=Canvas(screen,height=ht,width=wd,background="black")
canv.pack()
screenSaver(wd,ht)


screen.mainloop()
