# a=[1,2,3,4,5,6,7,8]
# m=0
# for i in a:
#     if i>=m:
#         m=+1
#     print(m)
# sum=0 
# for i in range(11):
#     sum +=i 
#     print(sum )

# for i in range(4):
#  a=int(input("enter the value of a"))
#  if(a>=1 and a<=10):
#   print("valid number")
# else:
#   print("invalid nummber")

#       armstrong number

a=int(input("enter the value of a:"))
m=0
s=str(a)
for i in range(len(s)):
    m+=int(s[i])**len(s)
    if m==a:
        print("armstrong number")
    else:
        print(" not armstrong number")

#                           while loop

n = int(input("Enter the number of terms: "))
a = 0
b = 1
count = 0
while count < n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count += 1

                   #  fabocani serize


n = int(input("Enter the number of terms: "))
a = 0
b = 1
count = 0
print("Fibonacci Series:")
while count < n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count += 1

def Hello(i="all",p=700):
    return (i,p)
Hello()




 