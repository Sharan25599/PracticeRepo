from array import *

val=array('i',[1,2,3,4,5])
#  Here "i"(integer)-> is the typecode, python type(int) and min size in byte(1)
val.reverse()
print(val)

val=array('i',[1,2,3,4,5])

for i in val:
      print(i)

newArr=array(val.typecode,(a for a in val))
# if we don,t know the typecode from an old  array we use val.typecode
for i in val:
      print(i)

vals=array('u',['a','e','i'])
# u -> unicode for characters
for i in vals:
    print(i)

# create an blank array
arr=array('i',[])
n=int(input("Enter the length of the array"))
for i in range(n):
    x=int(input("Enter the next value"))
    arr.append(x)
print(arr)

val=int(input("Enter the value for search "))
k=0
for e in arr:
    if e==val:
        print(k)
        break
    k=k+1
