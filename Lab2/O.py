def check_num(k):
    for i in k:
        int 

s = input()
list_str = ["ONE", "TWO" , "THR", "FOU", "FIV", "SIX", "SEV", "EIG", "NIN", "ZER"]
n = int((len(s)-1)/3)
print(n)
list_devides = []
g=0
c = ""
for i in range(len(s)):
    for j in range(3):
        c = c + s[g]
        g+=1
    list_devides.append(c)
    c= ""
    
#l1 = list_str[:n]
#print(l1)
print(list_devides)