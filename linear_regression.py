def linearRegression(xList,yList,origin=False):
    n=len(xList)
    sumXY=sum(xList[i]*yList[i] for i in range(n))
    sumX=sum(xList)
    sumY=sum(yList)
    sumXX=sum(i*i for i in xList)
    a1=(n*sumXY-sumX*sumY)/(n*sumXX-sumX*sumX)
    a0=(sumY-a1*sumX)/n
    if origin:
        a0=0
        a1=sumXY/sumXX
    return a0,a1