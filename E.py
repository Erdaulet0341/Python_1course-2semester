x, y = [int(x) for x in input().split()]
#x = int(input())
pr = False
for i in range(2, x):
    if x % i == 0:
        pr = True

if x <= 500 and y % 2 == 0 and pr==False:
    print("Good job!")
else:
    print("Try next time!")