#Cylotron Equations solved with odeint
#Beat Lauber

import numpy as np
from numpy import cos, sqrt
from scipy.integrate import odeint
import matplotlib.pyplot as plt

####################### relativistic Hamiltonian
def cyclo(y,t): #y[0]=x,1=px, 2=y, 3=py
    global a,w,rootc
    
    dx=(y[1]+y[2])/rootc(y)#np.sqrt(1+(y[1]+y[2])**2+(y[3]-y[0])**2)
    dpx=(y[3]-y[0])/rootc(y)#np.sqrt(1+(y[1]+y[2])**2+(y[3]-y[0])**2)
    dy=(y[3]-y[0])/rootc(y)#np.sqrt(1+(y[1]+y[2])**2+(y[3]-y[0])**2)
    dpy=(-y[2]-y[1])/rootc(y) + a*cos(w*t)#np.sqrt(1+(y[1]+y[2])**2+(y[3]-y[0])**2)
    return np.array([dx,dpx,dy,dpy])
    
    
def rootc(y): #function argument is a number
    return np.sqrt(1+(y[1]+y[2])**2+(y[3]-y[0])**2)
    
def rooth(y): #function argument is an array
    return np.sqrt(1+(y[:,1]+y[:,2])**2+(y[:,3]-y[:,0])**2)
    
def hamilton(y,t):
    global a,w
    return rooth(y)-a*y[:,2]*cos(w*t)


a,w=100,2 #parameter

time= np.linspace(0.0,100.0,10000)
yinit = np.array([1, 1,1,1]) #initial values
y = odeint(cyclo, yinit, time)


plt.figure()
plt.plot(time,hamilton(y,time),'b',label='relativistic')
#plt.title('cyclotron')
#plt.xlabel('Time')
#plt.ylabel('Hamiltonian')
#plt.show()
     


########################## non relativistic Hamiltonian

def cyclonr(y,t): #y[0]=x,1=px, 2=y, 3=py
    global w
    
    dx=y[1]+y[2]
    dpx=y[3]-y[0]
    dy=y[3]-y[0]
    dpy=-y[2]-y[1] + cos(w*t)
    return np.array([dx,dpx,dy,dpy])

    
def hamiltonnr(y,t):
    global w
    return 1/2*(y[:,1]+y[:,2])**2+1/2*(y[:,3]-y[:,0])**2-y[:,2]*cos(w*t)

ynr = odeint(cyclonr, yinit, time)


plt.plot(time,hamiltonnr(ynr,time),'g',label='non relativistic')
plt.title('cyclotron')
plt.xlabel('Time')
plt.ylabel('Hamiltonian')
plt.legend()
#plt.show()

plt.figure()
plt.plot(ynr[:,1],ynr[:,0],'g',label='non relativistic')
plt.title('cyclotron')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
