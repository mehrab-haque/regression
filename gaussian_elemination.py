import numpy as np

def gaussianElimination(A,B):
    n=A.shape[0]
    #Forward Elimination
    for i in range(n-1):
        for j in range(i+1,n):
            if A[i][j]==0: continue
            f=A[j][i]/A[i][i]
            A[j]=A[j]-A[i]*f
            B[j]=B[j]-B[i]*f

    #Back Substitution
    X=np.zeros(n,float)
    X[n-1]=B[n-1]/A[n-1,n-1]
    for i in range(n-2,-1,-1):
        sum_i=0
        for j in range(i+1,n):
            sum_i+=A[i][j]*X[j]
        X[i]=(B[i]-sum_i)/A[i][i]
    return X