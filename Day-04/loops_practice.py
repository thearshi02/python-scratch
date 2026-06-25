#problem1- multiplication table generator

num=int(input("enter the number"))
for i in range(1,10):
    print(f"{num} * {i} = {num*i}")



#problem-2 The guessing game challenge

secret = 7
while True:
    guess = int(input("enter guess number"))
    if (guess==secret):
        print("you guess the number")
        break
    else:
        print("wrong guess. Try again!!")