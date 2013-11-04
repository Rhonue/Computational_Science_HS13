#Legendre Polynomials, Week 7
#Program generates the first n legendre polynomials

 
from fivepoint import fivepoint
from scipy import *
from matplotlib import *
from pylab import *

n=5
 
def evalp(c,x):
    #evaluate a polinomial with parameter c at x
    sum=c[-1]
    for k in range(len(c)-1,0,-1):
        sum=x*sum+c[k-1]
    return sum
 
def ansatz(n):
    #generate an ansaz for the coefficients of the first n polynomials.
    P=[]
    for i in range(1,n+1,1):
        q=ones(i,float)
        P.append(q)
    return P
 
def normalise(P): #normalise a polinomial, P contains the coefficients of the polynomial
    for j in range(len(P)):
        P/=fivepoint(lambda x:evalp(P,x)**2,-1,1,10)**0.5
    return P
 
def gramschmidt(n):
    #generate n polynumials using the gram-schmidt orthonormal method
    #P array containig all the polinomial coefficients
    P=ansatz(n)
    for m in range(len(P)):
        for j in range(len(P[m])):
            for i in range(len(P[j])):
                
                P[m][i]-=fivepoint(lambda x:evalp(P[m],x)*evalp(P[j],x),-1,1,10)*P[j][i]
        P[m]=normalise(P[m])
    return P
 
def legendre(n):
    #generate the first n legendre polinomials using the integral normalisation criteria of the legendre polynomials
    P=gramschmidt(n)
    for i in range(len(P)):
        P[i]=1/(float(i)+1/2.0)**0.5*P[i]
    return P
 
if __name__ == '__main__':
    Coeffs=legendre(n)
    x=arange(-1,1,0.01)
    for i in range(len(Coeffs)):
        y=[]
        for j in range(len(x)):
            y.append(evalp(Coeffs[i],x[j]))
        plot(x,y)
    show()
