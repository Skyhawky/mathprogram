from lib.MathShapes import *
from lib.MathIndices import *
from Example.statsTest import Statistics
import os
from lib.MathIndices import Indices




def about_me () :

    print("*" * 40)
    print ('''* My name is finna
* I created  program for educational purposes.
* it is free to use :)
* This program is suitable for most ages''')
    print("*" * 40)

def selectionMenu():
    print('''
    What would you like to learn?
    press 1 for indices
    press 2 for shapes and area
    press 3 for statistics
    press q for quit
    ''')


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

    elif userInput == "q" :
        exit(0)
    

os.system("cls")





about_me ()


main()




