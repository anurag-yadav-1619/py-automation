# l=[-1,2,3,4,5,6,-5,-6,-7,-8,-98]
# print("positiv element are")
# for i in l:
#     if(i>=0):
#         print(i)

# print("nagative elements are")
# for i in l:
#     if(i<0):
#         print(i)


# a=[1,2,3,4,5,6,7,8,9]
# sum=0
# for i in a:
#     sum=sum+i
# print(sum/len(a))


# l=[3213,4124,432543,64563,234213,634564,2431,634534,3245,543546,6542324,546,5675756,746,2435,435436,5475876,8675,3456324]
# largest=l[0]
# index=0
# for i in range(len(l)):
#     if l[i]>largest:
#         largest=l[i]
#         index=i
# print(f"the largest element is {largest} at index{index}")

# l=[31,321,432,543,243,132,23,654,76,]
# largest=0
# sec_largest=l[0]
# for i in l:
#     if (i>largest):
#         sec_largest=largest
#         largest=i
#     elif(i>sec_largest):
#         sec_largest=i
# print(sec_largest,largest)
a=[1,2,3,4,5,6,7,8]
for i in range(len(a)):
    if a[i]<a[i+1]:
        continue
    else:
        print("you list is not sorted")
        break
else:
    print("your list is sorted")