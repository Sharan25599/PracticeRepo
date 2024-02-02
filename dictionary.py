fruit={"apple":50,"Banana":25,"Orange":40,"Grapes":70}
print(type(fruit))

# Extracting Keys
fruit={"apple":50,"Banana":25,"Orange":40,"Grapes":70}
print(fruit.keys())

# Extracting Values
fruit={"apple":50,"Banana":25,"Orange":40,"Grapes":70}
print(fruit.values())

print(fruit.items())

# adding new element
fruit={"apple":50,"Banana":25,"Orange":40,"Grapes":70}
fruit["Guava"]=100
print(fruit)

# popping an element(removing)
fruit={"apple":50,"Banana":25,"Orange":40,"Grapes":70,"Guava":100}
fruit.pop("Guava")
print(fruit)

# update one dict with another dict
fruit1={"apple":20,"orange":40}
fruit2={"cherry":30,"Banana":55}
fruit1.update(fruit2)
print(fruit1)

d1={"a":1,"b":2,"c":3}
if d1["b"]==2:
    d1["b"]=d1["b"]+100
print(d1)