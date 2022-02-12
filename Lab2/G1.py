n = int(input())
dic = {}

for i in range(n):
    l = input().split()
    s = l[0]
    x = l[1]
    if x not in dic.keys():
        dic[x] = 1
    else:
        dic[x] +=1
        
m = int(input())
for i in range(m):
    l = input().split()
    s = l[0]
    c = l[1]
    x = int(l[2])
    if dic[c] <= x:
        dic[c]=0
    else:
        dic[c] -= x
        
res = 0
for i in dic.values():
    res+=i

print('Demons left: ',res)
    