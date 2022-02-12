import math

def max1(arr):
    return abs(math.sqrt((arr[0]-x)*(arr[0]-x)+(arr[1]-y)*(arr[1]-y)))

l = input().split()
x = int(l[0])
y = int(l[1])
n = int(input())

arr=[]
for i in range(n):
    l1=input().split()
    x1=int(l1[0])
    y1=int(l1[1])
    arr.append((x1,y1))
    
arr.sort(key = max1)

for i in range(n):
    for j in range(2):
        print(arr[i][j], end = " ")
    print()    
    