l=[]
l1=[]
x=-1
cnt=0
while x!=1:
    s = input().split()
    l.append(s)
   # print(len(s))
    x = len(s)
t = tuple(l)
for i in range(len(t)):
    print(t[i][1])
    