#1. username is no more than 12 characters
#2. username must not contain any spaces
#3. username must not contain any special characters (only letters and numbers are allowed)

username = input("Enter a username: ")

if len(username) > 12:
    print("Error: Username must be no more than 12 characters.")
elif " " in username:
    print("Error: Username must not contain any spaces.")
elif not username.isalnum():
    print("Error: Username must not contain any special characters.")
else:
    print("Username is valid.")