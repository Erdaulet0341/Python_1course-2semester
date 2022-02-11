l = list(map(int, input().split()))
if(len(l)==1):
    k=int(input())
    m = l[0]
    l2 = list()
    for  i  in range(m):
        f=k + 2*i
        l2.append(f)
    sum=0
    for i in range(m):
        sum^=l2[i]
    print(sum)
else:
    k, t = l
    arr= []
    for i in range(k):
        h = t + 2*i
        arr.append(h)
    sum=0
    for i in range(k):
        sum^=arr[i]
    print(sum)
