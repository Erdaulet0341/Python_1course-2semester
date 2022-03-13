def check_prime(x):
    if n>1:
        for i in range(2, int(x/2)+1):
            if x%i==0:
                return False
        else:
            return True
    else:
        return False
    
def check_devise(x):
    cnt = 0
    for i in range(1, 10, 1):
        if x%i==0:
            cnt+=1
    if cnt == 1:
        return False
    else:
        return True

n = int(input())
if n == 0:
    print(10)
    exit()
if n == 1:
    print(1)
    exit()
arr = []
for i in range(10):
    l = 0
    arr.append(l)
    
for i in range(9, 0, -1):
    while n % i == 0:
        n/=i
        arr[i] += 1
        if n == 1:
            break
        elif check_prime(int(n))==True:
            break
        elif check_devise (int(n))==False:
            break
if n == 1:
    for i in range(2, 10, 1):
        while(arr[i]):
            arr[i]-=1
            print(int(i), end = '')
else:
    print(-1)