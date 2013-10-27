# Ex. 5.19
# Light house problem


import math as m
import numpy as np
from numpy import pi, arange, concatenate
from scipy import fft
from pylab import subplot, plot, show
import random as rand
import matplotlib as mplib

a=-0.5
b=0.7
phi=[]
for i in range(1000):
    phi+=[rand.random()*2*pi-pi]

x=np.array(a+b*np.tan(phi))
x = [i for i in x if abs(i) <= 1]
subplot(311)
mplib.pyplot.hist(x,bins=40)


a0=-1
b0=0.1

def prob(a,b):
    aa=-0.5
    bb=0.7
    phi=[]
    for i in range(1000):
        phi+=[rand.random()*2*pi-pi]

    x=np.array(aa+bb*np.tan(phi))
    x = [i for i in x if abs(i) <= 1]
    x=np.array(x)
    p=b/(a**2-2*a*x+b**2+x**2)/(np.arctan((1-a)/b)-np.arctan((-1-a)/b))
    p2=1
    for i in p:
        p2*=i
    return p2


alist=[]
blist=[]

for i in range(2000):
    ap=a0+((rand.random()-0.5)*0.1)
    bp=b0+((rand.random()-0.5)*0.1)

    if ap<-1:
        ap+=2
    if ap>1:
        ap-=2
    if bp<=0:
        bp+=1
    if bp>1:
        bp-=1
    if prob(a0,b0)==0:
        a0=ap
        b0=bp
        alist+=[a0]
        blist+=[b0]
    elif rand.random()<(prob(ap,bp)/prob(a0,b0)):
        a0=ap
        b0=bp
        alist+=[a0]
        blist+=[b0]
    else:
        alist+=[a0]
        blist+=[b0]

subplot(312)        
mplib.pyplot.hist(alist,bins=40)
subplot(313)
mplib.pyplot.hist(blist,bins=40)
show()

