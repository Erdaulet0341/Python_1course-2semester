n = int(input())
arr = []
for i in range(n):
    s = str(input())
    arr.append(s)
for i in range(n):
    if(arr[i].find("@gmail.com")>=0):
        k = len(arr[i])-10
        print(arr[i].replace("@gmail.com",""))
        