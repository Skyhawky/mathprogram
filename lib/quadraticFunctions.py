
def qFunc():
    print('''A quadratic function is f(x) = ax^2 + bx - c. Finding x is as simple as finding the factors of c that when summed give you b.
        Once you find the factors, add them to x 😀''')
        


def calFunc(c):
    listOfFactors = []
    rangeStart = 0
    rangeEnd = int(c)+1

    if c < 0:
        rangeStart = int(c-1)
        rangeEnd = 0


    for x in range(rangeStart, rangeEnd):
        try:
            if int(c)%x == 0:
                if int(c)>0:
                    listOfFactors.append(x)
                elif int(c)<0:
                    listOfFactors.append(x)
                    listOfFactors.append(x*-1)
                
        except ZeroDivisionError:
            pass

    return listOfFactors

def findB(b,listOfFactors):
    for i in range(len(listOfFactors)):
        for j in range(i+1,len(listOfFactors)):

            try:
                if listOfFactors[i]+listOfFactors[j] == b:
                    return(listOfFactors[i], listOfFactors[j])
                
            except IndexError:
                pass


            
    #write a function that finds b from list of c. calFunc calculates c list of factors. List of factors of i * 1+ list of factors for j. Else list of factors for i + list of factors of j *-1. Returns whatever worked including - values. Add input :)

    #Input is now working 👍

def main():
    qFunc()
    b = int(input("enter value b:"))
    c = int(input("enter value c:"))
    listOfFactors = calFunc(c)
    ans = findB(b,listOfFactors)
    print("The factors of the equation are: (x + ",ans[0],") (x +",ans[1],")")
    