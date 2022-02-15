def solve(numheads, numlegs):
    k = 4*numheads
    l=k-numlegs
    rabbit =  int(l /2)
    chicken = int(numheads - rabbit)
    print(f'Rabbits = {rabbit}')
    print(f'Chickens = {chicken}')

    
a,b=map(int, input().split())
solve(a,b)