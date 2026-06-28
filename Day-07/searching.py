#problem 1- Linear Search

list = [1,3,5,7,9,45,78,90]
target = 9
found = False
for i in range(len(list)):
    if(list[i]== target):
        found = True
        break
if(found == True):
    print("The targetted element is present in the list")
else:
    print("The element is not present in the list")        



#problem 2- Binary Search
list = [1,3,5,7,9,45,78,90]
target = 9
i=0
j=len(list)-1
while(i<=j):
    mid=(i+j)//2
    if(list[mid]==target):
        print("the element is found")
        break
    elif(list[mid]>target):
        j=mid-1
    else:
        i=mid+1  
else:
    print("element is not present")          

