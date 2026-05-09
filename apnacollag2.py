str1="this is srting. \n we are creating string  "
print(str1)
str1="anurag yadav"
print(())
str2=" yadav"
print(str1+str2)


str="anurag yadav"
print(str[-5:-1])

print(str[7])

str="i am from ghazipur from purfdsvanchal from utterpardash"
print(str.count("o"))
print(str)

name=input("enter your name : ")
print("length of your name is" ,len(name))

str="hi $i am the $ symbol $99.99"
print(str.count("9"))

                                        # condition statment

age=int(input("enter your age :"))
if (age<18):
    print("not eligibal for vote")
elif(age==18):
   print("can vote")

   {
    print("eligibal for vote")
}
   
marks=int(input("enter the  marks :"))
if(marks>=90):
    print("A+")
elif(marks>=80):
    print("A")
elif(marks>=70):
    print("B+")
elif(marks>=60):
    print("B")
elif(marks>=50):
    print("C+")
elif(marks>=40):
    print("C")
elif(marks>=30):
    print("D+")

elif(marks>=20):
    print("D")

else:
    print("E")


a=int(input("enter the number :"))
if(a%7==0):
    print("this number is devisibal by 7",True)
else:
     print("this number is not devisibal by 7",False)


                                            #  list &
                                            # tupple

        
list=[2,1,3]
# print(len(list))
# list.append(4)
print(list.sort())
# print(list)



list=[ 4,7,4,6,2]
print(list.append(5))
print(list.sort(reverse=True))
print(list)

list=['a','v','f','r','h']
# list.reverse()
list.insert(3,'t')
print(list)
                                            #   tuples


num=(3,5,4,6,7,8)
# print(type(num))
print(num[0])
print(num[1])

list1=[1,2,1]
list2=[1,2,3]
copy_list=list1.copy()
copy_list.reverse()
if(copy_list==list1):
    print("palindrome")
else:
    print("NOT a palindrome")


                    #   dictionary
                    
info={"name":"anurag yadav",
"class":"a",
"roll num":7,
}
print(type(info))




student={
    "name":"anurag",
    "subject":{
    "class":12,
    "phy":78,
    "math":89,
    }
    
}
# print(list(student.items()))
# print(student["subject"])
student.update({"city":"narwar"})
    
print(student)




                        #    set in python

collection=set()  
collection.add(1)
collection.add(2)
collection.add("anurag")
collection.add((1,2,3))
collection.clear(
)
print(len(collection))
 
collectin={"anurag","sujal","aman","amand"}
print(collectin.pop())
print(collectin.pop()) 
set1={1,2,3}
set2={3,4,5}
print(set1.union(set2))
print(set1)



marks={}

a=int(input("enter the marks of physics"))
marks.update({"physics":a})

b=int(input("enter the marks of chemistry"))
marks.update({"chem":b})

c=int(input("enter the marks of math"))
marks.update({"math":c})

d=int(input("enter the marks of english"))
marks.update({"english":d})

e=int(input("enter the marks of computer"))
marks.update({"computer":e})
print(marks )


                    #    loops

count=1
while count <=10:
    print("anurag")
    count+=1
    print(count)
 

i=5  
while i>=0:
    print(i)
    i-=1




i=1
while i<=10:
    print("i")
    i+=2
    
i=39
while i<=390:
    print(i)
    i+=39

num=[1,4,9,16,25,36,47,64,81,100]
idx=0
while idx <len(num):
    print(num[idx])
    idx+=1
                                #    break
i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i +=1

                                #  contanu
i=1
while i<=10:
    if(i%2==2):
        i+=2
        continue
    print(i)
    i+=2


num=[1,2,3,4,5]
for val in num:
    print(val)


range=[1,3,3,4,5,6]
for i in range:
    print (i)

str =["anurag yadav"]
for char in str:
    if (char=='r'):
        print("o is found")
        break
    print(char)
else:
    print("stop")


for i in range(1,10,2):
    print(i)

n=5

sum=0
for i in range(1, n+1):
    sum +=1
    
print("the sum is",sum)


                                        #  function


 
def anurag(a,b):
    sum =a+b
    print(sum)
    return sum
anurag(10,20)


def sujal(a,b):
    produ =a*b
    print("product")
    return
sujal(10,20)



def sujal(a,b,c,d,e):
    SI=(a+b+c+d+e)/5
    print(SI)
    return SI

sujal (91,93,85,93,96)

n=5
fact=1
for i in range(1,n+1):
    fact *=i
    print(fact)



def fact(n):
    fact = 1
for i in range(1,n+1):
    fact*=1
    print(fact)
    fact(5)

def converter(usa_valu):
    ind_valu=usa_valu*250
    print(usa_valu,"USA=",ind_valu,"IND")

converter(50)

                                    #    recursion




   









 














































































































