def reverse_sentences(arr):
    for i in range(len(arr)-1, -1, -1):
        print(arr[i], end=" ")

s = input().split()
reverse_sentences(s)


"""s
= input().split()
def f(arr):
    arr.reverse()
    return arr
print(*f(s))
"""
    
