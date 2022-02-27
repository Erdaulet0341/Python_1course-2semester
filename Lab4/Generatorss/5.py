from re import I


n = int(input())
def n_0(n):
    for i in range(n, -1, -1):
        yield i
        
print(*n_0(n))