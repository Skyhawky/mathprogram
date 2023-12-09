import matplotlib.pyplot as plt


def getValue(a,b,x):
    resultList = []
    for i in x:
        resultList.append(int(i)**2*a+b)
    return(resultList)

def computeNumbers2():
    print('''
    Non-Linear equation is represented as Ax^2 + B = 0, Ax^2 + By^2 = C , etc.
    ---------------------------------------------------------------
    In this example we will be representing one of those formulas, Ax^2 + B , to form a curved line on a non-linear graph :)
    ''')
    a = int(input("Input value of constant A:"))
    b = int(input("Input value of constant B:"))
    x = input("Input list value of variable x, with a comma between the values:").split(",")
    ans = getValue(a,b,x)
    plt.plot(ans)
    plt.show()