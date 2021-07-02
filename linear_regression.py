def linearRegression(xList,yList):
    n=len(xList)
    sumXY=sum(xList[i]*yList[i] for i in range(len(xList)))
    sumX=sum(xList)
    sumY=sum(yList)
    sumXX=sum(i*i for i in xList)
    a1=(n*sumXY-sumX*sumY)/(n*sumXX-sumX*sumX)
    a0=(sumY-a1*sumX)/n
    return a0,a1