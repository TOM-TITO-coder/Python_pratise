x = input("Enter number1: ")
y = input("Enter number2: ")

try:
    z = x / int(y)
except Exception as e:
    print("Error: ", e)
    z = None
except TypeError as e:
    print("Type Error: ", e)
    z = None
print("Division is: ", z)
