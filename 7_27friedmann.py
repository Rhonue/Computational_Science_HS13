#from math import cos, sin, pi
import numpy as np
#import scipy
import matplotlib
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from numpy import *

def fried1(a,H0,om,od):
    Ha=H0*sqrt(om/a**3+od)
    #tp=-1/(a*Ha)
    #rp=-tp/a
    return Ha

def fried2(Ha,a):
    #Ha=H0*sqrt(om/a**3+od)
    tp=-1/(a*1)
    #rp=-tp/a
    return tp

def fried3(Ha,a):
    #Ha=H0*sqrt(om/a**3+od)
    #tp=-1/(a*Ha)
    rp=-1/(a+a*Ha)
    return rp


def tp(k,a):
    [H0,om,od]=[1,1,1]
    Ha=H0*sqrt(om/a**3+od)
    return -1/(a*Ha)

def rp(k,a):
    [H0,om,od]=[1,1,1]
    Ha=H0*sqrt(om/a**3+od)
    return -1/(a*a*Ha)



#print(fried(1,1,1,1,3))
    

#[H0,om,od]=[1,1,1]
res1=odeint(tp,0,linspace(0.01,1,100))
res2=odeint(rp,0,linspace(0.01,1,100))

#print(res1)
#print(res2)

a=linspace(0.01,1,100)

plt.subplot(211)
plt.plot(a,res1)
plt.subplot(212)

plt.plot(a,res2)
plt.show()
