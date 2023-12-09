import webbrowser

def f(x):
    answer = x**2 + x
    print("f("+str(answer)+")")

f(2)

i = input("Press 1 to open reference link")

if(i == "1"):
    webbrowser.open("https://www.matrix.edu.au/beginners-guide-year-10-maths/part-6-year-10-functions/")