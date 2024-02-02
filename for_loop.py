l=['apple','Banana','Orange']
for i in l:
    print(i)

l=[1,2,3,4,5]
for i in l:
    print(i)

for i in range(5):
    print(i)

for i in range(2, 8):
    print(i)

for i in range(10):
    if i == 5:
        break
    print(i)

# nested for loop
l1=['orange','Blue','Green']
l2=['Book','chair','Phone']
for i in l1:
    for j in l2:
        print(i,j)