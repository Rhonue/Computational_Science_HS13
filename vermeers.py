

from numpy import *
from scipy.optimize import leastsq
import numpy as np




def func(p, grid, window):
    a,b,c,d=p[0],p[1],p[2],p[3]
    x=grid[0]
    y=grid[1]
    X=window[0]
    Y=window[1]
    err=(a*d-X*(x+c))**2+((x+b)*d-Y*(x+c))**2
    return err

#defining the grid
gridx=array([-1,0,1,-1,0,1,-1,0,1])
gridy=array([1,1,1,0,0,0,-1,-1,-1])
grid=array([gridx,gridy])

#defining the coordinates in pixels in the picture
windowx = array([59,77,92,59,77,93,60,78,93])
windowy = array([216,226,236,274,282,287,332,336,338])
window=array([windowx,windowy])

#start values
x0=np.array([ -2.58444336e-02,  -2.24788920e-01,  -2.46077762e-01,     2.79076875e+02])
#leastsquare fit 
xFit = leastsq(func, x0, args=(grid,window))
print(xFit)
print 'The distance between the viewer and the screen is', xFit[0][3], 'arbitrary units.'
  
  



