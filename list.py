l1=[1,"ABC",3.14,True]
print(l1[-1])
print(l1[1:4])

l1=[1,"a",2,"b",3,"c"]
l1.append("ABCD")
print(l1)

l2=[1,"a",2,"b",3,"c"]
l2.reverse()
print(l2)

l1=[1,2,3]
l2=[1,'a',True]
print(l1+l2)

l1=[1,'ABC',300]
print(l1*3)

l1=[1,2,3,4,5]
if l1[1]==2:
    l1[1]=l1[1]+100
print(l1)

l1=[1,2,3,4,5]
if l1[4]==10:
   l1[1]=l1[1]+100
else:
   l1[4]=l1[4]+500
print(l1)