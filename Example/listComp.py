oneToTen = [1,2,3,4,5,6,7,8,9,10]
oddNumbers = [x for x in oneToTen if x%2 != 0]
numLessThanFive = [x for x in oneToTen if x<5]
numGreaterThanTen = [x  if x>10 else "none" for x in oneToTen]

#number = int(input("enter number here:"))

multiplyNumber = lambda num: num*num

onePlusTwo = lambda : 1+2

greetings = lambda name: "hello "+name+"!"


def func(f,name):
    print(f(name))

repeat5 = lambda num: [x for x in range(1, num+1, 1)]

print(repeat5(4))