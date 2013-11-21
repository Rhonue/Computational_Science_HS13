#Black Hole Equations solved with odeint
#Beat Lauber, Ronny Ruettimann

import numpy as np
from numpy import sqrt
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def bhole(z,t): #0=x,1=px, 2=y, 3=py
    global rad
    #print z
    x,px,y,py=z[0],z[1],z[2],z[3]
    dx=(px*(rad(z)**3-2*x**2)-2*py*x*y)/rad(z)**3
    dpx=-x/(rad(z)*(rad(z)-2)**2)-((px*x+py*y)*(px*x**2+3*py*x*y-2*px*y**2))/rad(z)**5
    dy=(py*(rad(z)**3-2*y**2)-2*px*x*y)/rad(z)**3
    dpy=-y/(rad(z)*(rad(z)-2)**2)-((px*x+py*y)*(py*y**2+3*px*x*y-2*py*x**2))/rad(z)**5
    return np.array([dx,dpx,dy,dpy])
    
def rad(z):
    return np.sqrt((z[0])**2 + (z[2])**2)
    
def hamilton(z):
    global rad
    return 1/2*z[1]**2+1/2*z[3]**2-1/2*(1-2/rad(z))**(-1)-(z[0]*z[1]+z[2]*z[3])**2/rad(z)**3


if __name__=='__main__':
    zinit = np.array([100,0,100,0.1]) #initial values
    tend=10**6
    schritte=tend*10
    time= np.linspace(0.0,tend,schritte)        
    z = odeint(bhole, zinit, time)
    plt.figure()
    plt.plot(z[:,0],z[:,2])
    plt.title('Black Hole')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    #x=y=100, py=0.1, px=0 fuer gedrehte ellipsen
    #Observation: H<0 for all x,px,y,py
         
    
