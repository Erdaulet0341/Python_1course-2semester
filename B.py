s = input()
sum=0
for i in range(len(s)):
    k = ord(s[i])
    sum+=k
if sum>300:
    print("It is tasty!")
else:
    print("Oh, no!")