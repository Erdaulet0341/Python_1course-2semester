import random
import math

def generator_sqrt(n):
    for i in range(n):
        k = int(math.sqrt(i))
        if k*k==i:
            yield i
            
n = random.randrange(1,500)
it = generator_sqrt(n)
print(*it)
