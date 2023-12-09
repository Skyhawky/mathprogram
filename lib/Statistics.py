intList = []
numberList = []




def stats():
    print("Choose one to calculate:")
    options = input('''
    Press a for mean
    Press b for median
    mode is a work in progress (for now)
    ''')
    options.lower()
    if options == "a":
        mean()
    elif options == "b":
        median()

def prompt():
    numberList = input("Enter the data with a space between each number please")
    numberList = numberList.split()
    for item in numberList:
        intList.append(int(item))

def mean():
    prompt()
    print("The mean is the average. Which is the total sum of the values divided by the number of values")
    print("The mean is: ",sum(intList)/len(intList))




def median():
    prompt()
    print("The median is the middle number of a sorted list of data, or if you have an even amount of numbers it's the average of the two middle numbers")
    intList.sort()
    lengthOfNumList = len(intList)
    index = lengthOfNumList//2
    if lengthOfNumList%2 != 0:
        print("The median is: ",intList[index])
    else:
        print("The median is: ",(intList[index] + intList[index - 1])/2)
            
