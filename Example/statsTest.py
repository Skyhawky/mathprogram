
class Statistics:
    
    def __init__(self):   
        self.intList = []
        self.numberList = []




    def stats(self):
        print("Choose one to calculate:")
        options = input('''
        Press a for mean
        Press b for median
        mode is a work in progress (for now)
        ''')
        options.lower()
        if options == "a":
            self.mean()
        elif options == "b":
            self.median()

    def prompt(self):
        numberList = input("Enter the data with a space between each number please")
        numberList = numberList.split()
        for item in numberList:
            self.intList.append(int(item))

    def mean(self):
        self.prompt()
        print("The mean is the average. Which is the total sum of the values divided by the number of values")
        print("The mean is: ",sum(self.intList)/len(self.intList))




    def median(self):
        self.prompt()
        print("The median is the middle number of a sorted list of data, or if you have an odd amount of numbers it's the average of the two middle numbers")
        self.intList.sort()
        lengthOfNumList = len(self.intList)
        index = lengthOfNumList//2
        if lengthOfNumList%2 != 0:
            print("The median is: ",self.intList[index])
        else:
            print("The median is: ",(self.intList[index] + self.intList[index - 1])/2)
                