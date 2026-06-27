s="anurag yadav is a good boy"
print(type(s))
print(len(s))
print(s[0:26:1])

print(s[-1])
print(s[0])

a=[1,2,3,4]
print(a)
b=["green","for","green",4,5]
print(b)

a1=(1,2,3,4)
print(a1)


print(type(True))
print(type(False))


set1=(["geeks","for","geeks"])
print(set1)
print(len(set1))
for i in set1:
    print(i,end=" ")
print("anurag",i,end=" ")



d={1:"anurag ",2:"vfiudsbni",3:"svndfuh"}
print(d)

d={1:"vmdkp",'name':"anurag",3:"vmefodsnv"}
print(d[1])
print(d[3])

a=1
b=2
c=a
print(a is  c)
print(b)
b+=a
print(b)



count =1
while count<=10:
    print("count :",count)
    count+=1


for letter in "python":
    if letter=="h":
        pass
    print(letter)

def fun(a,b):
    print(a+b)
fun(1,1)


def anurag(x):
    if(x%2==0):
        print("even")
    else:
        print("odd")

anurag(10)

def anurag(x,y=10):
    print("x",x)
    print("y",y)
anurag(1)



def anurag(an,bn):
    print(an,bn)
anurag(an="anurag",bn="sujal")
anurag(bn="sujal",an="anurag")


def position(name,age):
    print("hi,i am",name)
    print("my age is ",age)


print("Case-1:")
position("anurag",15)
print("\nCase-2")
position(15,"anurag")


correct_password="anuragyadav"
attempts=0
while attempts<3:
    pwd=input("enter the password : ")
    if pwd==correct_password:
        print("access granted")
        break
    else:
        print("incorrect password")
        attempts+=1

if attempts==3:
    print("try after some time")



for i in range(1, 5):
 for j in range(i):
  print("*", end=" ")
  print() 























