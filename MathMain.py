from lib.MathShapes import *
from lib.MathIndices import *
from Example.statsTest import Statistics
import os
import webbrowser
from lib.MathIndices import Indices
import lib.linear as linear
import lib.nonlinear as nonlinear
import lib.circle as c
import lib.quadraticFunctions as quad


def about_me () :

    print("*" * 40)
    print ('''* I am skyhawk
* I created  program for educational purposes.
* it is free to use :)
* This program is suitable for most ages''')
    print("*" * 40)

def selectionMenu():
    print('''
    What would you like to learn?
    Press 1 for indices
    Press 2 for shapes and area
    Press 3 for statistics
    Press 4 for non linear equations
    Press 5 for linear equations
    Press 6 for circular equations
    Press 7 for quadratic equations
    Press q for quit
    press r for references
    ''')

def refsFunc():
    r = input('''
Press the listed numbers/letter combinations to go to a reference
Section 1: indices
******************
i1
i2
Section 2: Shapes and area
**************************
sh1
sh2
Section 3: Statistics
*********************
s1
s2
Section 4: Non-linear equations
*******************************
nl1
Section 5: Linear equations
***************************
l1
Section 6: Circular equations
*****************************
c1
Section 7: Quadratic equations
******************************
q1
''')
    if(r=="i1"):
        webbrowser.open("https://www.mathsisfun.com/definitions/index-power-.html")
    elif(r=="i2"):
        webbrowser.open("https://byjus.com/maths/index/")
    elif(r=="sh1"):
        webbrowser.open("https://www.khanacademy.org/math/cc-third-grade-math/imp-geometry/imp-multiply-to-find-area/a/area-rectangles-review")
    elif(r=="sh2"):
        webbrowser.open("https://www.mathsisfun.com/geometry/circle-area.html")
    elif(r=="s1"):
        webbrowser.open("https://www.mathsisfun.com/mean.html")
    elif(r=="s2"):
        webbrowser.open("https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/mean-median-basics/a/mean-median-and-mode-review")
    elif(r=="nl1"):
        webbrowser.open("https://www.mathsisfun.com/definitions/nonlinear-equation.html")
    elif(r=="l1"):
        webbrowser.open("https://www.mathsisfun.com/algebra/linear-equations.html")
    elif(r=="c1"):
        webbrowser.open("https://www.mathsisfun.com/algebra/circle-equations.html")
    elif(r=="q1"):
        webbrowser.open("https://www.mathsisfun.com/algebra/quadratic-equation.html")

def shouldContinue() :
    willContinue = input("Do you want to continue learning? [y/n]")
    if willContinue == "y" :
        os.system("cls")
        main()
    else :
        exit(0)


def main () :
    
    stat = Statistics()
    selectionMenu()
    userInput = input()

    if userInput == "1" :   
        Indices.printIndices()
        shouldContinue()

    elif userInput == "2" :
        shapes()
        shouldContinue()
        
    elif userInput == "3":
        stat.stats()
        shouldContinue()

    elif userInput == "4" :
        nonlinear.computeNumbers2()
        shouldContinue()
        
    elif userInput == "5":
        linear.computeNumbers()
        shouldContinue()  

    elif userInput == "6":
        c.calculateVal()
        shouldContinue()

    elif userInput == "7":
        quad.main()

    elif userInput == "r":
        refsFunc()

    elif userInput == "q" :
        exit(0)


os.system("cls")



about_me ()


main()


#Go through your application and make it more user-friendly, and it is good enough to use it as a study reference.
#It has to help and be useful :)
