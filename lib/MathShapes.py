import turtle
from math import pi
import time


#this is turtle pensize when writing on the screen
penSize = 10

def triangle (tside) :
    turtle.pensize(penSize)
    for i in range(3) :
        turtle.forward(tside)
        turtle.left(120)
    thieght = tside * 3 / 2
    area = thieght * tside / 2
    return area


def circle (radius) :
    turtle.pensize(penSize)
    turtle.circle(radius)
    area =  pi * pow(radius,2)
    return area



def square (hieght) : 
    turtle.pensize(penSize)
    for i in range(4) : 
        turtle.forward(hieght)
        turtle.left(90)
    area = pow(hieght,2)
    return area



def rectangle(hieght, length) : 
    turtle.pensize(penSize)
    for i in range(2) : 
        turtle.forward(hieght)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
    area = length * hieght
    return area


def write(shapeWanted, area) :
    turtle.penup()
    x,y = turtle.pos()
    turtle.goto(x - 100,y - 100)
    turtle.write("The area of the {} is: {}".format(shapeWanted, area))
    time.sleep(5)
    return

def check (shape) :
    if  shape > 150 or shape < 50 :
        print("Please enter a number within the size limit (50 - 150)")
        shapes()
    
def shapes() :
    shapeWanted = input("Circle or rectangle or square:")
    shapeWanted = shapeWanted.lower()
    if shapeWanted == "circle" :
        wantedRadius = int(input ("Your radius here:"))
        check(wantedRadius)
        area = circle(wantedRadius)
    

    elif shapeWanted == "square" :
        side = int(input ("Your side length here:"))
        check(side)
        area = square(side)

    elif shapeWanted == "rectangle" :
        hieght = int(input("Your hieght here:"))
        check(hieght)
        length = int(input("your length here:"))
        check(length)
        area = rectangle(int(hieght), int(length))
    
    elif shapeWanted == "triangle" :
        tside = int(input("triangle side here:"))
        check(tside)
        area  =  triangle(tside)
    write(shapeWanted,area)
    turtle.bye()