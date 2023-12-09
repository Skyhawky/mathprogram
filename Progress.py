from time import sleep

print("[",end='', flush=True)
for i in range (10):
    print("*",end='', flush=True)
    sleep(0.5)

print("]",end='', flush=True)