#Cylotron Equations solved with odeint
#Beat Lauber

import numpy as np
from numpy import cos, sqrt
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def cyclo(y,t): #0=x,1=px, 2=y, 3=py
    global a,w,rootc
    
    dx=(y[1]+y[2])/rootc(y)#np.sqrt(1+(y[1]+y[2])**2+(y[3]-y[0])**2)
    dpx=(y[3]-y[0])/rootc(y)#np.sqrt(1+(y[1]+y[2])**2+(y[3]-y[0])**2)
    dy=(y[3]-y[0])/rootc(y)#np.sqrt(1+(y[1]+y[2])**2+(y[3]-y[0])**2)
    dpy=(-y[2]-y[1])/rootc(y) + a*cos(w*t)#np.sqrt(1+(y[1]+y[2])**2+(y[3]-y[0])**2)
    return np.array([dx,dpx,dy,dpy])
    
    
def rootc(y):
    return np.sqrt(1+(y[1]+y[2])**2+(y[3]-y[0])**2)

    
def rooth(y):
    return np.sqrt(1+(y[:,1]+y[:,2])**2+(y[:,3]-y[:,0])**2)
    
def hamilton(y,t):
    global a,w,rooth
    return rooth(y)-a*y[:,2]*cos(w*t)


a,w=1,1

time= np.linspace(0.0,100.0,10000)
yinit = np.array([1, 1,1,1]) #initial values
y = odeint(cyclo, yinit, time)

#print len(time)
#print len(y[0])

plt.figure()
plt.plot(time,hamilton(y,time))
plt.title('cyclotron')
plt.xlabel('Time')
plt.ylabel('Hamiltonian')
plt.show()
     

