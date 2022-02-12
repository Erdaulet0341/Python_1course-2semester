n = int(input())
arr = []
disks = []
for i in range(n):
    k=input().split()
    if len(k)==2:
        arr.append(k[1])
    else:
        disks.append(arr.pop(0))
        
print(*disks, end=" ")
