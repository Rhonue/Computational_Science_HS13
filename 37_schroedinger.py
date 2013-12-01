# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 13:09:24 2013

@author: ruettir
"""

from math import cos, sin, pi, e
from numpy import fft
import numpy as np
from numpy import *
import numpy.fft as ft
import scipy
import matplotlib
import matplotlib.pyplot as plt
from tkinter import *

def schroedinger(psi,x):
    return None
    
  
def potential(x):
    x=x*0
    x[len(x)//2]=10**8
    x[len(x)//2+1]=10**8
    x[len(x)//2-1]=10**8
    #x=1/2* abs(x*x-1)**2 # double well potential
    return np.array(x)

'''forschlaufe
    psi=e**()*psi
    fft(psi)
    psi=e**()*psi
    ifft(psi)
    psi=e**()*psi'''


def pseudofrosch(x,k,tmax,dt):
    global potential, psi0
    ti=[0]
    fi=[psi0(x)]
    mmax=int((tmax)/dt+1)
    for m in range(1,mmax,1):
        tn=ti[m-1]
        fn=fi[m-1]
        fn=np.array(fn)
        dp1=e**(-1j*potential(x)*dt/2)*fn #
        
        
        ft_fn=ft.fft(dp1) #falschrum
        ft_fn=ft.ifftshift(ft_fn)
        
        dp2=e**(-1j*1/2*k**2*dt)*ft_fn
        
        ift_fn=ft.ifft(dp2)
        ift_fn=ft.ifftshift(ift_fn)
        dp3=e**(-1j*potential(x)*dt/2)*ift_fn
        
        dp3=list(dp3)
        
        ti+=[tn+dt]
        fi=fi+[dp3]
    return [ti,fi]
    
if __name__ == '__main__' :
    
    
    xmax=2**8
    xmin=-xmax
    dx=0.1
    kmax=pi/dx
    kmin=-kmax
    dk=pi/xmax
    tmax=30
    dt=0.5
    xx=np.arange(xmin,xmax+dx,dx)
    kk=np.arange(kmin,kmax+dk,dk)
    
    def psi0(x):
        global xmax
        #a gaussian wave packet of width a, centered at x0, with momentum k0
        a=10
        x0=-xmax/4
        k0=30
        return ((a * np.sqrt(np.pi))**(-0.5)* np.exp(-0.5*((x-x0)*1./a)**2 + 1j*x*k0))#list(np.zeros(xmax/dx))+[1]+list(np.zeros(xmax/dx))
    
    #print len(xx), len(kk), len(psi0)
    [t,psiend]=pseudofrosch(xx,kk,tmax,dt)
    
    tt=np.array(t)
    psiend=np.array(psiend)
    xend=0 #abs(*) < xmax
    tend=1 #< tmax
    psiendtime=psiend[:,(xend+xmax)/dx]  #time evolution at one space coordinate
    psiendtimereal=real(psiendtime)
    psiendtimeimag=imag(psiendtime)
    
    psiendspace=psiend[tend/dt,:]        #space evolution at one time point
    psiendspacereal=real(psiendspace)
    psiendspaceimag=real(psiendspace)
    
    ########################## Tkinter animation

    master = Tk()

    wd, ht=master.winfo_screenwidth(), master.winfo_screenheight()
    w = Canvas(master, width=wd, height=ht)
    w.pack()

    for k in range(len(tt)//2):
        psiendspace=psiend[k*2,:]
        psiendspacereal=real(psiendspace)
        w.delete(ALL)
        
        for i in range(len(xx)-1):
            x0=(xx[i]-xx[0])*wd/(xx[-1]-xx[0]) #scale the points to draw
            y0=(psiendspacereal[i]*ht+ht/2)
            x1=(xx[i+1]-xx[0])*wd/(xx[-1]-xx[0])
            y1=(psiendspacereal[i+1]*ht+ht/2)
            w.create_line(x0, y0, x1, y1, fill="blue")
        w.update()


    mainloop()


'''  
    plt.subplot(411)
    plt.plot(tt,psiendtimereal)
    plt.subplot(412)
    plt.plot(xx,psiendspacereal)
    plt.subplot(413)
    plt.plot(tt,psiendtimeimag)
    plt.subplot(414)
    plt.plot(xx,psiendspaceimag)
    plt.show()

   '''
