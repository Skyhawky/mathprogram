
class Animal:
    def __init__(self, colour, country): #colour is a parameter of the init function
        self.colour = colour 
        self.country = country    #will be visible to all functions in class

    def seeColour(self):     #self makes it available to the function
        print(self.colour)

    def setColour(self,colour):
        self.colour = colour



class Dog(Animal):
    def getLegs(self):
        print(4)

d = Dog("black and white","africa")

d.seeColour()
d.getLegs()

class greyhound(Dog):
    pass
g = greyhound
g.getLegs()
g.seeColour()