

import math as m
import numpy as np
from numpy import pi, arange, concatenate
from scipy import fft
from pylab import subplot, plot, show
import random as r
import matplotlib

s=[]
N=100

for j in range(10000):
    d=0
    for i in range(N):
        d+=r.randrange(-1,2,2)

    s+=[d]

s=np.array(s)
#s=abs(s)


matplotlib.pyplot.hist(s, bins=N/10, range=None, histtype='bar')
show()
