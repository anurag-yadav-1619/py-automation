a=int(input("enter the marks 1"))
b=int(input("enter the marks 2"))
c=int(input("enter the marks 3"))
d=int(input("enter the marks 4"))
e=int(input("enter the marks 5"))
x=a+b+c+d+e
print(x)
p=(x/500)*100
print(p)
if(p>=91):
    print("a+")
elif(p>=81 and 90>=p):
    print("b")
elif(p>=71 and 80>=p):
    print("c")
elif(p>=61 and 70>=p):
    print("d")
elif(p>=51 and 60>=p):
    print("e")
else:
    print("F")
