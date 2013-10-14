# Ex. 4.13
# Fast Fourier Transform


import math as m
import numpy as np
from numpy import pi, arange, concatenate
from scipy import fft
from pylab import subplot, plot, show

N=pow(2,6)
L=8
dx=2.*L/N
x=np.array((arange(N)-N/2)*dx)
k=np.array(2*pi/(N*dx)*(arange(N)-N/2))
f= 1/(1+x*x)
F=fft(f)
F= concatenate((F[N/2:N],F[0:N/2]))

subplot(222)
plot(x,f)
subplot(221)
plot(k,F.real,'b.')
plot(k,F.imag,color='magenta')



x=np.array((arange(N))*dx)
f= 1/(1+x*x)
k=np.array(2*pi/(N*dx)*(arange(N)))
def w(k,N):
    return np.exp( (2*pi*k/N)*1j)

def rfft(f):
    n=len(f)
    if n==1:
        return f
    else:
      Feven = rfft([f[i] for i in range(0, n, 2)])
      Fodd = rfft([f[i] for i in range(1, n, 2)])
 
      combined = [0] * n
      for m in range(n//2):
         combined[m] = Feven[m] + w(m,n) * Fodd[m]
         combined[m + n//2] = Feven[m] - w(m,n) * Fodd[m]
 
      return combined

  
G=np.array(rfft(f))
G= concatenate((G[N/2:N],G[0:N/2]))
subplot(223)
plot(k,G.real,'b.')
plot(k,G.imag,color='yellow')
#subplot(224)

show()
