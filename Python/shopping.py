item = input("Enter the item you want to buy: ")
quantity = input("Enter the quantity: ")
price = input("Enter the price per item: ")

quantity = int(quantity)
price = float(price)

total = quantity * price
print(f"Total cost for {quantity} {item}(s): ${total:.2f}")