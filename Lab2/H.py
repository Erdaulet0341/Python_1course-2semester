x,y=map(int, input().split())
n = int(input())
l1=list()
d = int(n/2)
for i in range(2):
    for j in range(d):
        k,m=map(int, input().split())
        l1.append((k,m))
import math
l2=[]
for i in range(2):
    for j in range(d):
        g=math.sqrt((l1[i][j]-x)*(l1[i][j]-x)+(l1[j][i]-y)*(l1[j][i]-y))
        l2.append(g)
print(l2)