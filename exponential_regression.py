from math import *
from bisection import bisect
from visuals import plot

def exponentialRegression(xList,yList):
    n=len(xList)
    def syebx(b):
        return sum(yList[i]*exp(b*xList[i]) for i in range(n))
    def se2bx(b):
        return sum(exp(2*b*x) for x in xList)
    def sxyebx(b):
        return sum(xList[i]*yList[i]*exp(b*xList[i]) for i in range(n))
    def sxe2bx(b):
        return sum(x*exp(2 * b * x) for x in xList)
    def func(b):
        return sxyebx(b)-syebx(b)*sxe2bx(b)/se2bx(b)
    b=bisect(func,-0.5,-0.05,50,0.005)
    a=syebx(b)/se2bx(b)
    def plotFunction(x):
        return a*exp(b*x)
    plot(xList,yList,plotFunction)
    return a,b


