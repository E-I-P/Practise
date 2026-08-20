# logical operators = evaluate multiple conditions in a single statement. They are used to combine conditional statements and return a boolean value (True or False). The three main logical operators in Python are:
# 1. and: Returns True if both conditions are True.
# 2. or: Returns True if at least one of the conditions is True.
# 3. not: Returns True if the condition is False, and vice versa.


# example 1: Using the "and" operator
age = 25
has_license = True

if age >= 18 and has_license:
    print("You are eligible to drive.")
else:
    print("You are not eligible to drive.")

# example 2: Using the "or" operator
temperature = 30
is_sunny = True

if temperature > 25 or is_sunny:
    print("It's a nice day!")
else:
    print("It's not such a nice day.")

# example 3: Using the "not" operator
is_raining = False

if not is_raining:
    print("It's not raining.")
else:
    print("It's raining.")