

# def divide(para,parb):
#     ans = para/parb
#     return ans


# while True:
#     num1 = input("First number")
#     num2 = input("Second number")

#     try:
#         print(divide(int(num1),int(num2)))
#     except ZeroDivisionError:
#         print("Infinity")
#     except ValueError:
#         print("Please enter integer")
#     except OverflowError:
#         print("Please enter a smaller number")


class OneDivisionError(Exception):
    pass

try:
    raise(OneDivisionError)
except OneDivisionError:
    print("yes")