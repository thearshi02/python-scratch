#problem 1- the dynamic guest list

guests=["Alice", "Bob", "Charlie"]
guests.append("David")
guests[1]="Eve"
length=len(guests)
print(guests)
print(f"there are {length} guests")



#problem 2- Inventory slicing and auditing 

inventory=["laptop", "mouse", "keyboard","monitor", "hdmi_cable"]
peripheral = inventory[1:4]
inventory.pop(-1)
print(f"updated inventory:{inventory} and the peripheral list: {peripheral}")
