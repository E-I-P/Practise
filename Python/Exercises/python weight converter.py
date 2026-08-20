weight = float(input("Enter your weight in kilograms: "))

if weight > 0:
    result = weight * 2.205
    print(f"Your weight is {result:.2f} pounds.")
else:
    print("Please enter a valid weight.")