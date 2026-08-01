import random
num=random.randint(1,11)
print("welcome to our game")
while True:
    guess=int(input("guess the number :"))
    if guess<num:
        print("too low, roo the lowest number")
    elif guess>num:
        print("too high, goo to larges numbre")
    else: 
        print("congratulations, you won the game")
        break
    