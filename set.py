
# Duplicates are not allowed in set
s1={1,"Hemanth","Hemanth",1}
print(s1)

# There is no proper sequence in set so,the indexing is not possible in set
s1={1,"a",True,2,"abc",False}
s1.add("hello")
print(s1)

s1={1,"a",True,2,"abc",False}
s1.update([10,20,30])
print(s1)

s1={1,"a",True,2,"abc",False,"b"}
s1.remove("b")
print(s1)

# union and intersection
s1={1,2,3}
s2={"a","b","c"}
print(s1.union(s2))

s1={1,2,3,4,5,6}
s2={5,6,7,8,9}
print(s1.intersection(s2))
