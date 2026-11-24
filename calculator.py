#Easy calculator using python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

#Now we will take input from the user, this part is the main function of the calculator
#In this part we increase the functionality of the calculator by adding more operations and also we will add error handling for invalid inputs

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice(1/2/3/4): ")

if choice in ['1', '2', '3', '4']:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        add_result = add(num1, num2)
        print(f"{num1} + {num2} = {add_result}")
    elif choice == '2':
        subtract_result = subtract(num1, num2)
        print(f"{num1} - {num2} = {subtract_result}")
    elif choice == '3':
        multiply_result = multiply(num1, num2)
        print(f"{num1} * {num2} = {multiply_result}")
    elif choice == '4':
        divide_result = divide(num1, num2)
        print(f"{num1} / {num2} = {divide_result}")
else:
    print("Invalid input")