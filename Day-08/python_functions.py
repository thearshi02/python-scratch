#problem 01- Modularizing your search algorithm

#linear search
def linear_search(target_list,target):
    result=-1
    for index, value in enumerate(target_list):
        if(value==target):
            result = index
            return index
            break
    return -1

# binary search
def binary_search(target_list,target):
    result =-1
    min=0
    max=len(target_list)-1
    while(min<=max):
        mid=(min+max)//2
        if(target_list[mid]==target):
            result = mid
            return mid   
            break
        elif(target_list[mid]>target):
            max = mid-1
        else:
            min = mid+1  
    return result

list=[1,2,3,4,6,7,9,34,56,78,89,99]
target = 34
ans1 = linear_search(list,target)
ans2 = binary_search(list,target)
print(f"the index of the target element is {ans1} which is found by linear search")
print(f"the index of the target element is {ans2} which is found by binary search")
