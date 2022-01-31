s = str(input())
c = str(input())
k = s.count(c)
if k <= 1:
    print(s.find(c))
else:
    print(s.find(c), end=' ')
    print(s.rfind(c))