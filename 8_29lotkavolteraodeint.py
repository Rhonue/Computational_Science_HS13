#Lotka Volterra Equations solved with odeint
#Beat Lauber

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def lotka(y,t):
    a=10
    dx= a*y[0]-y[0]*y[1]      #dx/dt
    dy= y[0]*y[1]-y[1]       #dy/dt
    return np.array([dx,dy])


time= np.linspace(0.0,10.0,1000)
yinit = np.array([10, 10]) #initial values
y = odeint(lotka, yinit, time)

plt.figure()
plt.plot(y[:,0],y[:,1])
plt.title('Lotka-Volterra Equations')
plt.xlabel('No. of ducks')
plt.ylabel('No. of fox')
plt.show()
     
''' for a=y and x=1, the popolation of both duck and fox remain constant'''
