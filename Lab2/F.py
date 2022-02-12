n = int(input())
dic = {}

for i in range(n):
    l = input().split()
    k = l[0]
    x = int(l[1])
    if k in dic.keys():
        sum = dic[k] + x
        dic[k]=sum
    else:
        dic[k]=x

max=-1e9
for i in dic.values():
    if i>max:
        max=i

l = []
for i in dic.keys():
    l.append(i)
l.sort()

for i in l:
    mx=dic[i]
    res=max-mx
    if res==0:
        print(f'{i} is lucky!')
    else:
        print(f'{i} has to receive {res} tenge')