import math
import matplotlib.pyplot as plt
import numpy


def calculateVal():

    print('''circle formula: x^2 + y^2 = r^2    or    x^2 -b + y^2 - a = r^2
genertae x data caluctulate y data
Assuming the radius  = 25
y^2 =  r^2 - x^2
y = sqrt(r^2 - x^2) and y = -sqrt(r^2 - x^2)''')

    x = []
    y = []
    r = 0


    r = 0
    while r<5:
        r = int(input("Enter a radius that is greater than or equal to 5:"))



    def calculateYVal(R,X):
        Y = math.sqrt(R**2 - X**2)
        return Y

    def calculateYMinusVal(R,X):
        Y = -math.sqrt(R**2 - X**2)
        return Y

    for i in numpy.arange(-r,r+0.1,0.1):
        x.append(i)
        y.append(calculateYVal(r,i))

    for i in numpy.arange(r,-r - 0.1,-0.1):
        x.append(i)
        y.append(calculateYMinusVal(r,i))
        

    plt.plot(x,y)
    plt.show()