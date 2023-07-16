f = open("cool.txt","r")
y = []

for x in f.readlines():
    if not x.isnumeric():
        y.append(x.strip())

f.close()
print(y)