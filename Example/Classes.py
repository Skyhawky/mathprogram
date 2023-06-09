

class Car():
    def __init__(self,colour,type) -> None:
        self.colour = colour
        self.type = type

    def getMyColour(self):
        print(self.colour)
    def getType(self):
        print(self.type)

myCar = Car("red","sport")
myCar.getMyColour()
myCar.getType()

myTeachersCar = Car("blue","not sport")
myTeachersCar.getMyColour()
myTeachersCar.getType()