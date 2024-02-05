# Slicing with List values
l=[22,11,32,24,46,57,68,77]
   #0, 1, 2, 3, 4, 5, 6, 7
   # -7,-6,-5,-4,-3,-2,-1

# from 3rd index to last 2nd index(7->it exclude the last index)
print(l[3:7])

# from 0 index to nth index
print(l[0:])

# from 0 index to last second index
print(l[:-1])

# from 3rd index value to last 2nd index value using (-neg index)
print(l[-5:-1])

# from 2nd index value to last 2nd index value using (+ve and -ve index)
print(l[1:-2])

# get copy of entire list
print(l[:])

# list[start:end:step] step-> 2 prints every second value in list
print(l[2:-1:2])

#from 0 index to last second index, step->3 prints every third value in the list
print(l[0:-1:3])

# from last index to third index, step->-1 in reverse order
print(l[-1:2:-1])

# reverse the list
print(l[::-1])


# Slicing with string values

str='LearningChamp'

# starts from 8th index to nth index
print(str[8:])

# reverse the string
print (str[::-1])

# from 0 index to 8th index(8th index not included)
print(str[0:8])

# complete index
print(str[0:])
print(str[:13])
print(str[:])

# from 0 index to 8th index(step-> 2 - gives every 2nd character)
print(str[0:8:2])

# gives every 2nd character in str from 0 index to last index
print(str[::2])

# to get a single character
print(str[8:9])