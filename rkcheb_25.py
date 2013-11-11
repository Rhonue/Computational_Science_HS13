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

def cheb(x,T0,T1,n):
    '''RHS of ODE's T0 is function, T1 is 1st diff'''
    if x==-1:
        x+=0.01
    if x==1:
        x-=0.01
    H0=T1 #d/dx
    H1=1/(1-x*x)*(x*T1 -n*n*T0) #d/dx
    return np.array([H0,H1])


def rk4(cheb,xmin,xmax,x,T0,T1,n,dx):
    
    if xmax==1:
        xmax-=dx
    if xmin==-1:
        xmin+=dx
    t0i=[T0]
    t1i=[T1]
    xi=[x]
    mmax=int( (xmax-xmin)/dx +1)
    for m in range(1,mmax,1):
        xn=xi[m-1]
        t0n=t0i[m-1]
        t1n=t1i[m-1]
        
        dt1=dx*cheb(xn,t0n,t1n,n)
        dt10=dt1[0]
        dt11=dt1[1]
    
        dt2=dx*cheb(xn+dx/2.0, t0n+dt10/2.0, t1n+dt11/2.0,n)
        dt20=dt2[0]
        dt21=dt2[1]
    
        dt3=dx*cheb(xn+dx/2.0, t0n+dt20/2.0, t1n+dt21/2.0,n)
        dt30=dt3[0]
        dt31=dt3[1]
    
        dt4=dx*cheb(xn+dx, t0n+dt30, t1n+dt31,n)
        dt40=dt4[0]
        dt41=dt4[1]
    
        xi+=[xn+dx]
        t0i+=[t0n+(1.0/6)*(dt10+2.0*dt20+2.0*dt30+dt40)]
        t1i+=[t1n+(1.0/6)*(dt11+2.0*dt21+2.0*dt31+dt41)]
        
    return [xi,t0i,t1i]

if __name__ == '__main__' :
    
    n=5
    [xmin,xmax,dx] = [-1.0, 1.0, 0.001]
    [x0, T0, T1] = [xmin, cos(n*pi/2), n*sin(n*pi/2)]

    [x,TT0,TT1] = rk4(cheb, xmin, xmax, x0, T0, T1, n, dx)
    plt.subplot(211)
    plt.plot(x,TT0)
    plt.subplot(212)
    plt.plot(x,TT1)
    plt.show()