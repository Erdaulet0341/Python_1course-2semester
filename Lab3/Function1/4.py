def filter_prime(arr): #7 8 9
    cnt = 0
    l=[]
    for i in range(len(arr)):
        k=int(arr[i])
        if k==1:
            continue                    
        for j in range(2, k-1):       
            if k%j==0:
                cnt+=1
        if cnt == 0:
            l.append(k)
        cnt=0
    return l

print()
list_numbers = input().split()
print(*filter_prime(list_numbers))
