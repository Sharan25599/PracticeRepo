from functools import reduce

# To sort elements in the list ascending order
l=[11,24,43,35,65,45,77,8]
l.sort()
print(l)

# To sort elements in the list descending order
l=[11,24,43,35,65,45,77,8]
l.sort(reverse=True)
print(l)

# reverse the list using slicing
l=[11,24,43,35,65,45,77,8,99,101]
rev_l=l[::-1]
print(rev_l)

# To multiply the elements in list
l=[11,24,43,35,65,45,77,8]
result=1
for i in l:
    result=result*i
print(result)


# Without using sort()
data_list=[24,122,68,77,53,45,21]
new_list=[]
while data_list:
    minimum=data_list[0]
    for x in data_list:
        if x>minimum:
            minimum=x
    new_list.append(minimum)
    data_list.remove(minimum)
print(new_list)

# To print fibonacci number
def F(n):
   if n == 0: return 0
   elif n == 1: return 1
   else: return F(n-1)+F(n-2)

for i in range(0,12):
    print(F(i))

# To print list in reverse
l=[22,31,1,23,12,45,10,5]
print(l[::-1])

l=[22,31,1,23,12,45,10,5]
def rev(li):
    return li[::-1]
print(l)


# To check whether string is palindrome or not(Malayalam)
str=input("Enter the str:")
revstr=(str[::-1])
# using slicing reverse the string (str[::-1])
if revstr==str:
    print("Str is palindrome")
else:
    print("Str is not palindrome")


# To check Prime or Not
# natural number>1
# which has only 2 factors (1 and itself)
num=int(input("Enter a number:"))
count=0
for i in range(1,num+1):
    if num%i == 0:
        count=count+1
if count==2:
    print("Num is Prime")
else:
    print("Num is not Prime")

# Find sum of elements in array
arr=[1,2,3,4,5,6,7]
print(sum(arr))
# add or sub value to the above array
print(sum(arr)+10)
print(sum(arr)-10)

# To find max and min element in an array
arr=[21,3,32,43,11,55,77]
max=arr[0]
n=len(arr)
for i in range(1,n):
    if arr[i]>max:
        max=arr[i]
print(max)

arr=[21,3,32,43,11,55,77]
min=arr[0]
n=len(arr)
for i in range(1,n):
    if arr[i]<min:
        min=arr[i]
print(min)

# To swap first and last element in list
l=[11,23,32,43,54,65,77]
n=len(l)

temp=l[0]
l[0]=l[n-1]
l[n-1]=temp

print(l)
# or
l[0],l[-1]=l[-1],l[0]
print(l)

# To reverse a String
word="Captain cool"
print(word[::-1])
# (or)
# using lambda func
rev=reduce(lambda x,y:y+x,word)
print(rev)

# To check string is Anagram or Not
str1=input("Enter the String1:")
str2=input("Enter the String2:")
if len(str1) != len(str2):
    print("Not anagram")
elif sorted(str1) == sorted(str2):
    print("Strings are Anagram")
else:
    print("Not Anagram")

# To find maximum between three numbers.
a=int(input("Enter the value1: "))
b=int(input("Enter the value2: "))
c=int(input("Enter the Value3: "))
if a>b and a>c:
    print("A is greater",a)
elif b>a and b>c:
    print("B is greater",b)
elif c>a and c>b:
    print("C is greater",c)
else:
    print("Some numbers are identical cannot compare to give greater please check the values")

# To enter base and height of a triangle and find its area.
base=int(input("Enter the base of the triangle: "))
height=int(input("Enter the height of the triangle: "))
area=(1/2)*base*height
print("Area of Triangle: ",area)


