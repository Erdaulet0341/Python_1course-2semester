n = -1
l = []
while n != 0:
    k = int(input())
    l.append(k)
    n = k
l1 = []
k = len(l) - 2
for i in range(int(len(l) / 2)):
    g = l[i] + l[k]
    l1.append(g)
    k -= 1
    
if len(l) % 2 == 0:
    l1[len(l1) - 1] = int(l1[len(l1) - 1] / 2)

print(*l1)