import numpy as np
from math import *
from gaussian_elemination import gaussianElimination

def polynomialRegression(xList,yList,m):
    n=len(xList)
    coeffArr=np.ndarray((m+1,m+1))
    constArr=np.ndarray((m+1,1))
    for i in range(m+1):
        for j in range(m+1):
            coeffArr[i][j]=sum(pow(x,i+j) for x in xList)
        constArr[i]=sum(pow(xList[ind],i)*yList[ind] for ind in range(n))
    return gaussianElimination(coeffArr,constArr)