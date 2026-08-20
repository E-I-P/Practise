# format specifiers = {index:flags} format a value based on what flags are inserted

price = 49.999987
price2 = 5.99
price3 = -23.78

print("The price is: ${:.2f}".format(price))  # formats the price to 2 decimal places
print("The price is: ${:.2f}".format(price2))  # formats the price to 2 decimal places
print("The price is: ${:.2f}".format(price3))  # formats the price to 2 decimal places
