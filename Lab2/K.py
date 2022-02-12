def f(x):
    k = ''
    for i in x:
        if i == '.':  # Boris!
            k=k
        elif i == ',':
            k=k
        elif i == '!':
            k=k
        elif i == '?':
            k=k
        else:
            k += i
    return k


s = input().split()
st = set()
for i in s:
    x = f(i)
    st.add(x)
l = list(st)
l.sort()
print(len(l))
for i in l:
    print(i)
