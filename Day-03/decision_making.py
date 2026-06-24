#problem1- Age classifier and ticketing

age=int(input("enter you age"))
if(age<12):
    print("Ticket category : Chilf(free)")
elif(age>12 and age<=64):
    print("Ticket Category: Adult($10)")
else:
    print("Ticket category:Senior($5)")



#problem2-Odd or Even Checker

number = int(input("Enter any whole number"))
if(number%2==0):
    print(f"the {number} is even number")
else:
    print(f"the {number} is odd number")    
            