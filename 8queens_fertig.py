from itertools import permutations

n = 8
N=1
ivec={}
cols =range(n)
for vec in permutations(cols):
    if (n == len(set(vec[i]+i for i in cols))
          == len(set(vec[i]-i for i in cols))):
        ivec[N]=list(vec)
        N+=1
        #print(vec)


       
for i in ivec:
    for k in range(n):
        ivec[i][k]= (2*k-7)+ (2*ivec[i][k]-7)*1j
z=len(ivec)
print('There are', z, 'solutions,')  

#sort out double solutions
for i in range(1,z):
    for k in range(i+1,z+1):
        try:
            if all((ivec[k][l])*1j in ivec[i] for l in range(n) ) :
                del ivec[k]
            if all((ivec[k][l])*(-1) in ivec[i] for l in range(n) ) :
                del ivec[k]
            if all(ivec[k][l]*(-1j) in ivec[i] for l in range(n) ) :
                del ivec[k]
            if all((ivec[k][l]).conjugate() in ivec[i] for l in range(n) ) :
                del ivec[k]
            if all((ivec[k][l]).conjugate()*(-1) in ivec[i] for l in range(n) ) :
                del ivec[k]
            if all((ivec[k][l]).conjugate()*1j in ivec[i] for l in range(n) ) :
                del ivec[k]
            if all((ivec[k][l]).conjugate()*-1j in ivec[i] for l in range(n) ) :
                del ivec[k]
        except KeyError:
            pass

print('but only', len(ivec), 'unique solutions:')       
for i in ivec:
    print((list(ivec[i])))
