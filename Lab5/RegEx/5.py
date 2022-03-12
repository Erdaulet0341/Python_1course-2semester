import re

s = input()
x = re.search("b$", s)
y = re.search("^a", s)

if x and y:
    print("Yes")
else:
    print("No")