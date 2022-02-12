s = input()
l = []
for i in range(len(s)):
    if len(l)==0:
        l.append(s[i])
    else:
        if (s[i] == ')') and (l[len(l)-1]=='('): #()
            l.remove('(')
        elif (s[i] == ']') and (l[len(l)-1]=='['): #()
            l.remove('[')
        elif (s[i] == '}') and (l[len(l)-1]=='{'): #()
            l.remove('{')
        else:
            l.append(s[i]) 

if len(l)==0:
    print("Yes")
else:
    print("No")