import math
def max1(arr):
    return abs(math.sqrt((arr[0]-x)*(arr[0]-x)+(arr[1]-y)*(arr[1]-y)))

x,y = map(int,input().split())
n = int(input())

arr=[]
for i in range(n):
    x1,y1=map(int,input().split())
    arr.append((x1,y1))
    
arr.sort(key = max1)

for i in arr:
    print(*i)