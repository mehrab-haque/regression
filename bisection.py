max_iter=20
prevRoot = 0

def bisect(func,lowerBound,upperBound,iteration,maxErrorPercentage):
    global prevRoot
    if iteration==0:
        return prevRoot
    currentRoot=(upperBound+lowerBound)/2
    errorPercentage = abs(((currentRoot-prevRoot)*100/currentRoot))
    if iteration<max_iter and errorPercentage<=maxErrorPercentage:
        prevRoot=currentRoot
        return currentRoot
    if func(currentRoot)==0:
        return currentRoot
    elif func(lowerBound)*func(currentRoot)<0:
        upperBound=currentRoot
    else:
        lowerBound=currentRoot
    prevRoot=currentRoot
    return bisect(func,lowerBound,upperBound,iteration-1,maxErrorPercentage)