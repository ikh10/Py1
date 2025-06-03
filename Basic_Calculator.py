print("Basic Calculator: ")

#Input for 2 numbers and select operation to be performed 
num1 = float(input("Enter the first num: "))
num2 = float(input("Enter the second num: "))
op = input("Choose an op (+, -, *, /): ")

if op == '+':
    res = num1 + num2
    print(f"Result: {res}")
elif op == '-':
    res = num1 - num2
    print(f"Result: {res}")
elif op == '*':
    res = num1 * num2
    print(f"Result: {res}")
elif op == '/':
    if num2 == 0:
        print("Error: Div by zero not allowed.")
    else:
        res = num1 / num2
        print(f"Result: {res}")
else:
    print("Invalid op selected.")
