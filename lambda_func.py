# add the num
a=lambda x,y,z:(x+y+z)
print(a(4,5,6))

# Multiply the nums
a=lambda x,y:x*y
print(a(5,5))

# larger num
larger=lambda x,y:x if(x>y) else y
print(larger(27,47))

# Square the nums
nums=[2,3,4,5,6,7]
squared_list=list(map(lambda x:x**2,nums))
print(squared_list)

# print even numbers
nums=[2,3,7,22,12,16,17]
even_list=list(filter(lambda x:x%2==0,nums))
print(even_list)



