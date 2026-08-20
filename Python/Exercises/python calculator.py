num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result:.2f}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result:.2f}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result:.2f}")
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result:.2f}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator. Please use +, -, *, or /.")