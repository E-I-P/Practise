# string methods = functions that manipulate strings

name = "John"
print(name.upper())  # converts the string to uppercase
print(name.lower())  # converts the string to lowercase
print(name.title())  # converts the string to title case
print(name.capitalize())  # capitalizes the first letter of the string
print(name.strip())  # removes leading and trailing whitespace
print(name.replace("John", "Jane"))  # replaces a substring with another substring
print(name.split(","))  # splits the string into a list of substrings
print(name.join(["Hello", "World"]))  # joins a list of strings with the original string
print(name.startswith("J"))  # checks if the string starts with a specific substring
print(name.endswith("n"))  # checks if the string ends with a specific substring
print(name.find("o"))  # returns the index of the first occurrence of a substring
print(name.count("o"))  # counts the number of occurrences of a substring
print(name.isalpha())  # checks if the string contains only alphabetic characters
print(name.isdigit())  # checks if the string contains only digits
print(name.isalnum())  # checks if the string contains only alphanumeric characters
print(name.islower())  # checks if the string is in lowercase
print(name.isupper())  # checks if the string is in uppercase
print(name.isspace())  # checks if the string contains only whitespace
print(len(name))  # returns the length of the string