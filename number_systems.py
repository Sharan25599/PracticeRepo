bin(25)
print(bin(25))
# 0b11001  0b-> represents as binary

print(oct(21))
#0o25      0o-> represents as octal

print(hex(21))
# 0x15     0x-> represents as hexadecimal

# swap 2 variables

a=6
b=5
temp=a
a=b
b=temp
print("a =",a)
print("b =",b)

a=6
b=7
a=a+b
b=a-b
a=a-b
print("a =",a)
print("b =",b)

a=25
b=31
a,b=b,a
# its just rotates the value
print("a =",a)
print("b =",b)