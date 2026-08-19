#input() = a function that prompts the user to enter data and returns the input as a string

name = input("What is your name? ")
age = input("What is your age? ")

age = int(age) #Typecasting string to int

print(f"Hello, {name}!")
print(f"You are {age} years old.")