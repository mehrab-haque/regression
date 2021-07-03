import numpy as np
from matplotlib import pyplot as plt

def plot(xList,yList,func,sharpness=1000,marginPercentage=2):
    plt.scatter(xList,yList,color="red",marker=1)
    range=max(xList)-min(xList)
    xListNew=list(np.linspace(min(xList)-range*marginPercentage/100,max(xList)+range*marginPercentage/100,sharpness))
    yListNew=[func(x) for x in xListNew]


    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')

    plt.plot(xListNew, yListNew)
    plt.show()
