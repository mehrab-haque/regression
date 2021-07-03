
def readPoints(fileName):
    file = open(fileName, 'r')
    Lines = file.readlines()
    xList=[]
    yList=[]
    for line in Lines:
        xList.append(float(line.split()[0]))
        yList.append(float(line.split()[1]))
    return xList,yList

