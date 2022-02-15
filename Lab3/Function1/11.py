def check_palindrome(s): #qazaq
    ok = True
    k = len(s)-1 #4
    for i in range(int(len(s)/2)): #1
        if s[i]!=s[k]:
            ok= False
            return ok
        k-=1
    return ok
            
s = input()
if check_palindrome(s)==True:
    print("Palindrome")
else:
    print("Not palindrome")