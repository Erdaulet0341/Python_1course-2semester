n = int(input())
arr = []
disks = []
for i in range(n):
    k = input()
    if k[0] =='1':
        arr.append(k[2:len(k)])
        #print(arr[i])
    else:
        g = arr[0]
        arr.pop(0)
        #print(arr[0])
        disks.append(g)
        
print(*disks, end=" ")
