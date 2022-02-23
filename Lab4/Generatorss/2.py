n = int(input())
def even_gen(n):
    for i in range(n):
        if i%2==0:
            yield i
            
it = even_gen(n)
print(*it, sep = ", ")