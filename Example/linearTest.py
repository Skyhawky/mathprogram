import matplotlib.pyplot as plt
from math import sin,cos

def sineList(parameters):
    sinList = []
    for i in parameters:
        sinList.append(sin(i))
        
    return sinList

def cosineList(parameter):
    cosinList = []
    for i in parameter:
        cosinList.append(sin(i))
        
    return cosinList

plt.plot(sineList([1,2,3,4,5,6,7,8,9,10]),cosineList([-4,-3,-2,-1,0,1,2,3,4,5]))
plt.show()