# Normal Functions
def even_odd(x):
    if x%2==0:
        print(x,"is even")
    else:
        print(x,"is odd")
even_odd(5)

def add10(x):
    print(x+10)
add10(10)


# Lambda Function
g=lambda x:x*x*x
print(g(7))

# lambda function with filter
l1=[5,7,22,97,54,62,77,23,73,6]
a=list(filter(lambda x:(x%2 != 0),l1))
print(a)

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)

words = ["apple", "banana", "cherry", "date"]
long_words = filter(lambda word: len(word) > 5, words)

# lambda function with Map
numbers = [1, 2, 3, 4]
squared= map(lambda x: x**2, numbers)

names = ["Apple", "Banana", "Orange"]
uppercase= map(lambda name: name.upper(), names)

# map applies a function to each item, filter selects items based on a condition,
# and reduce combines items iteratively(reducing it to a single value).


# lambda function with reduce
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)

words = ["hello", " ", "world"]
sentence = reduce(lambda x, y: x + y, words)

a="Alpha"
reverse=reduce(lambda x,y:y+x,a)
print(reverse)

# map applies a function to each item, filter selects items based on a condition,
# and reduce combines items iteratively(reducing it to a single value).
