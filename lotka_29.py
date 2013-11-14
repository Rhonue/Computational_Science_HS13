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

def lotka(t,x,y,a):
    dx= a*x-x*y      #dx/dt
    dy= x*y-y       #dy/dt
    return np.array([dx,dy])


def rk4(lotka,tmin,tmax,t,x,y,a,dt):
    
    xi=[x]
    yi=[y]
    ti=[t]
    mmax=int( (tmax-tmin)/dt +1)
    for m in range(1,mmax,1):
        tn=ti[m-1]
        xn=xi[m-1]
        yn=yi[m-1]
        
        dz1=dt*lotka(t,xn,yn,a)
        dx1=dz1[0]
        dy1=dz1[1]
    
        dz2=dt*lotka(tn+dt/2.0, xn+dx1/2.0, yn+dy1/2.0,a)
        dx2=dz2[0]
        dy2=dz2[1]
    
        dz3=dt*lotka(tn+dt/2.0, xn+dx2/2.0, yn+dy2/2.0,a)
        dx3=dz3[0]
        dy3=dz3[1]
    
        dz4=dt*lotka(tn+dt, xn+dx3, yn+dy3,a)
        dx4=dz4[0]
        dy4=dz4[1]
    
        ti+=[tn+dt]
        xi+=[xn+(1.0/6)*(dx1+2.0*dx2+2.0*dx3+dx4)]
        yi+=[yn+(1.0/6)*(dy1+2.0*dy2+2.0*dy3+dy4)]
        
    return [ti,xi,yi]

if __name__ == '__main__' :
    
    a=10.
    [tmin,tmax,dt] = [0, 10, 0.001]
    [x, y, t] = [1, 10, 0]

    [tt,xx,yy] = rk4(lotka, tmin, tmax, t, x, y, a, dt)
    q=1
    if q==0:
        #plt.subplot(211)
        plt.plot(tt,xx,'g',label='duck')
        #plt.subplot(212)
        plt.plot(tt,yy,'r',label='fox')
        plt.legend()
        plt.show()
    else:
        plt.plot(xx,yy,'g-o',label='x=duck')
        plt.legend()
        plt.show()
        
        ''' for a=y and x=1, the popolation of both duck and fox remain constant'''