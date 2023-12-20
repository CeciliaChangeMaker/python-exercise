
def addition(x, y):
    return x + y
def substraction(x, y):
    return x - y
def multiplication(x, y):
    return x * y
def division(x, y):
    return x / y

print("Welcome to Calculator")
print()

while True:
    print("Select operation: \n (1) Addition \n (2) Substraction \n (3) Multiplication \n (4) Division \n")
    operation = input("Enter your choice (1/2/3/4): ")
    num1 = float(input("Enter your first number:"))
    num2 = float(input("Enter your second number: "))

    if operation == '1':
        print("Output is: ", addition(num1, num2))
    elif operation == '2':
        print("Output is: ", substraction(num1, num2))
    elif operation == '3':
        print("Output is: ", multiplication(num1, num2))
    elif operation == '4':
        print("Output is: ", division(num1, num2))
    else:
        print("Invalid Operation")
        print("----")
        print()

