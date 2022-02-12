def f(s):
    cnt=tnt=dnt=0
    for i in s:
        if 65<=ord(i)<=90:
            cnt+=1
        elif 97<=ord(i)<=122:
            tnt+=1
        elif 48<=ord(i)<=57:
            dnt+=1
    if cnt>0 and tnt>0 and dnt>0:
        return True
    else:
        return False

n = int(input())
s = set()
for i in range(n):
    x = input()
    if f(x)==True:
        s.add(x)

l = list(s)  
l.sort()
print(len(l))
for i in l:
    print(i)
