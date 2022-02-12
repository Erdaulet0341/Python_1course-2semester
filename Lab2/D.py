n = int(input())
if n%2==0:
    for i in range(n):
        for j in range(1+i): 
            print('#', end="")
        for j in range(n-1-i):
            print('.', end="")
        print()
else:
    for i in range(n):
        for j in range(n-1-i):
            print('.', end="")
        for j in range(1+i):
            print('#', end="")
        print()