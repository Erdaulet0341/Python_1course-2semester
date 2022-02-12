n = int(input())
dem = {}

for i in range(n):
    d_name,weak=input().split()
    if weak not in dem:
        dem[weak]=1
    else:
        dem[weak]+=1

m = int(input())
hun = {}

for i in range(m):
    h_name, patron, x = input().split()
    if patron not in hun:
        hun[patron]=int(x)
    else:
        hun[patron]+=int(x)
        
cnt=0

for i in dem:
    if i in hun:
        dem[i]-=hun[i]
    if dem[i]>0:
        cnt+=dem[i]
        
print("Demons left:", cnt)