#Problem 1
item_name = input("Enter the name of the item")
price = input("enter the price of the item")
quantity = input("enter the quantity of the item")
price=float(price)          #typecasting
quantity=int(quantity)       #typecasting
total_cost = price*quantity
print(f"you bought {quantity} of {item_name} for a total of {total_cost} ")


#problem 2 
first_name=input("enter the first name")
last_name=input("enter the last name")
fullname=first_name+last_name       #concatanation
print(f"welcome {fullname}")