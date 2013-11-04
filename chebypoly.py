from legendrepoly import ansatz, evalp
from newtoncotes import fivepoint
from scipy import *
from matplotlib import *
from pylab import *
 
def normalisecheby(P):
  
    for j in range(len(P)):
        P/=fivepoint(lambda x:evalp(P,x)**2/((1-x*x)**0.5),-1,1,10)**0.5
    return P
 
def gramsmitdcheby(n):
    P=ansatz(n)
    for m in range(len(P)):
        for j in range(len(P[m])-1):
            for i in range(len(P[j])):
                tmp = fivepoint(lambda x:evalp(P[m],x)*evalp(P[j],x)/((1-x*x)**0.5),-1,1,10)
                P[m][i]-=tmp*P[j][i]
        P[m]=normalisecheby(P[m])
    return P
 
def chebychev(n):
   
    P=gramsmitdcheby(n)
    P[0]=pi**0.5*P[0]
    for i in range(1,len(P)):
        P[i]=(pi/2)**0.5*P[i]
    return P
 
if __name__ == '__main__':
    Coeffs=chebychev(5)
    x=arange(-1,1,0.01)
    for i in range(len(Coeffs)):
        y=[]
        for j in range(len(x)):
            y.append(evalp(Coeffs[i],x[j]))
        plot(x,y)
    show()