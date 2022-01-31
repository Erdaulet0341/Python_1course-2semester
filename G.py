s = str(input())
n = 0
k = len(s)
f = k-1
sun = 0
for i in range(k):
    p = int(s[i])*(2**f)
    f=f-1
    sun+=p
print(sun)