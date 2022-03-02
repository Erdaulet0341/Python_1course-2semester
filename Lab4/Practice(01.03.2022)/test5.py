
def calc(a, b, s):
    if s=='+':
        return a+b
    elif s == '-':
        return a- b
    elif s == "*":
        return a *b
    elif s == '/':
        return a/b
    else:
        return "Incorrect value"

n = int(input())
k = int(input())
s = input()
print(calc(n, k, s))