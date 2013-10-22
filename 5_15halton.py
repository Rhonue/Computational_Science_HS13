import math as m
import numpy as np
from numpy import pi, arange, concatenate
from scipy import fft
from pylab import subplot, plot, show


N=512


def convert(N,b):
    halton=[]
    for i in range(1,N):
        n=i
        k=[0]
        while (n>0):
            a=int(float(n%b))
            k.append(a)
            n=(n-a)/b
        
        string=""
        e=0
        z=0
        for j in k[::1]:
            z+=j*b**e
            e-=1
        halton+=[z]
        
    return halton


halton2= convert(N,2)
halton3= convert(N,3)
plot(halton2,halton3,'b.')
show()
