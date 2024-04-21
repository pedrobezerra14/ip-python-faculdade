li1 = [1,2,3,4,5,8,9]
li2 = [1,2,3,4,5,6,7,]
li3 = []

for i in li1:
    if i not in li2:
        li3.append(i)
        
for i in li2:
    if i not in li1:
        li3.append(i)
        
        
print(li3)
