n = int(input())
arr = []
for i in range (n):
    k = int(input())
    arr.append(k)
arr.sort()
print(arr[n-2]*arr[n-1])