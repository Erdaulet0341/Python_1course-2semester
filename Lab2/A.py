l = list(map(int, input().split()))
pos=len(l)-1 #4

for i in  range(len(l)-2,-1,-1):
    if i+l[i]>=pos:
        pos=i

if pos==0:
    print(1)
else:
    print(0)