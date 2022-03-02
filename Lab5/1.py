dic = {'ONE':'1', 'TWO':'2', 'THR':'3', 'FOU':'4' , 'FIV':'5',
       'SIX':'6', 'SEV':'7', 'EIG':'8', 'NIN':'9','ZER':'0'}

def f(s):
    cnt = 0
    c = l = ''
    for i in range(len(s)):
        if i == len(s)-1:
            cnt+=1
            c+=s[i]
        if cnt == 3:
            for j in dic:
                if j == c:
                    l+=dic[j]
                    c = s[i] 
                    cnt = 1
        else:
            c+=s[i]
            cnt+=1
    return l

s = input().split('+')
sum = int(f(s[0]))+int(f(s[1]))
st = str(sum)
k = ''
for i in st:
    for j in dic:
        if i == dic[j]:
            k+=j
print(k)