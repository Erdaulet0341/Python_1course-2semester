from itertools import permutations

def print_permutation(s):
    p = permutations(s)
    for i in p:
        for j in i:
            print(j,end='')
        print()
s = input()

print_permutation(s)