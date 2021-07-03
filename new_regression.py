from math import *
from visuals import plot

def newRegression(xList,yList):
    n=len(xList)
    syex=sum(yList[i]*exp(xList[i]) for i in range(n))
    sxx=sum(x*x for x in xList)
    sxy=sum(xList[i]*yList[i] for i in range(n))
    sxex=sum(x*exp(x) for x in xList)
    se2x=sum(exp(2*x) for x in xList)
    b=(syex*sxx-sxy*sxex)/(se2x*sxx-sxex*sxex)
    a=(sxy-b*sxex)/sxx
    def plotFunction(x):
        return a*x+b*exp(x)

    plot(xList, yList, plotFunction)
    return a, b