import random

print("Hello! What is your name?")
s = input()
print()
print(f'Well, {s}, I am thinking of a number between 1 and 20.')
print("Take a guess.")
k = random.randrange(1,20)
x=-1
cnt=0

while x != k:
    n = int(input())
    print()
    if n < k:
        print('Your guess is too low.')
        print("Take a guess.")
    else:
        print('Your guess is too bigger.')
        print("Take a guess.")
    x=n
    cnt+=1
print(f'Good job, {s}! You guessed my number in {cnt} guesses!')
    
    







"""x = random.randint(1,9) # 1-3  contains 3
print(x)
#           Random functions
#       <1>  choice(seq) :
print(random.choice(range(10)))

#       <2> randrange([start, stop, [step])
print(random.randrange(0, 100))"""