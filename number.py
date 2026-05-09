import random 
num=random.randint(1,11)
guess=int(input("please guess the number :- "))
print(num)
if guess==num:
    print("you are wright")
else:
    ("sorry,you are wrong")
