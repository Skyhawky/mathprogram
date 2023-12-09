import matplotlib.pyplot as plt


def getValue(a,b,x):
    resultList = []
    for i in x:
        resultList.append(int(i)*a+b)
    return(resultList)

def computeNumbers():
    print('''
    Linear equation is represented as Ax + B = 0, Ax + Ay = C, etc.
    ---------------------------------------------------------------
    In this example we will be representing one of those formulas, Ax + B, to form a line on a linear graph :)
    ''')
    a = int(input("Input value of constant A:"))
    b = int(input("Input value of constant B:"))
    x = input("Input list value of variable x, with a comma between the values:").split(",")
    ans = getValue(a,b,x)
    plt.plot(ans)
    plt.show()