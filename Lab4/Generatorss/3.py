n = int(input())

def divide4_3(n):
    for i in range(n):
        if i%3==0 and i%4==0:
            yield i
            
it = divide4_3(n)
print(*it)