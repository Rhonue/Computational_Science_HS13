from matplotlib.image import imread
from pylab import imshow, contour, show
from time import time
from numpy import *

s_per_hour = 60*60.
s_per_day  = 24.*s_per_hour
s_per_year = 365.242*s_per_day
inclination = 23.5/180*pi
equinox12 = 1332331200.0  # reference time, time.time() at 12:00 UTC, 20. März 2012, 

def plot_map(name):
    img = imread(name)
    imshow(img)
    return img.shape[0:2]

def daylight(longitude, latitude, t):
    beta = (((t/s_per_day)/s_per_hour)/24)*2*pi
    delta = (t/s_per_year)*2*pi
    
    ez = matrix([[1,0,0]])
    
    ez = ez*rot_y(latitude)
    ez = ez*rot_z(longitude+delta+beta)
    ez = ez*rot_x(inclination)
    ez = ez*rot_z(-delta)
    return ez[0,0]

    

def get_time():
    return time()-equinox12

def rot_x(w):
    m = matrix([[1,0,0], [0,cos(w),sin(w)], [0,-sin(w),cos(w)]])
    return m
    
def rot_y(alpha):
    m = matrix([[cos(alpha), 0, -sin(alpha)], [0,1,0], [sin(alpha), 0, cos(alpha)]])
    return m
    
def rot_z(w):
    m = matrix([[cos(w),sin(w),0], [-sin(w),cos(w),0], [0,0,1]])
    return m

x = linspace(0,800,50)
y = linspace(400,0,50)
scale = linspace(0,1,10)
xb = linspace(-pi,pi,50)
yb = linspace(-pi/2,pi/2,50)
i = 0
j = 0
t = get_time()
z = zeros((50,50))

for wx in xb:
    i = 0
    for wy in yb:
        zi = daylight(wx,wy,t) 
        z[i,j] = zi
        i += 1
    j += 1
         
mape = plot_map('plate-carree.png')
contour(x,y,z,scale)
show()





