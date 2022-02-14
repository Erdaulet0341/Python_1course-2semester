n=input()
l=[]

for i in n:
    if len(l)==0:
        l.append(i)
        if l[0]=='}' or l[0]==']' or l[0]==')':
            print('No')
            exit(0)
    elif len(l)!=0:
        if l[-1]=='[' and i==']' or l[-1]=='{' and i=='}' or l[-1]=='(' and i==')':
            l.pop()
        else:
            l.append(i)
            
if len(l)==0:
    print('Yes')
else:
    print('No')


"""def isBalanced(s):
    arr = []
    brackets = {'{':'}', '[':']', '(':')'}
    for char in s:
        if char in ('{', '[', '('):
            arr.append(char)
        else:
            if arr:
                top = arr.pop()
                if brackets[top] != char:
                    return 'No'
            else:
                return 'No'
    return 'No' if arr else 'Yes'
    s = str(input())
    print(isBalanced(s))         
   """