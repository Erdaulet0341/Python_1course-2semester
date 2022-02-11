l1 = [i for i in range(10)]
print(l1)

l2 = [i for i in range(2, 21, 2)]
print(l2)

list3 = list()
for i in range(1,3):
    for j in range(3):
        list3.append((i,j))
        
for i in range(1,3):
    for j in range(3):
        print(list3[i])
    print()
    
list4 = [(i,j) for i in range(0,2) for j in range(3)]
for i in range(1,3):
    for j in range(3):
        print(list4[i])
    print()