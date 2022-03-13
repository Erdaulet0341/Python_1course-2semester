import re


s = input()
l = re.split('(?=[A-Z])',s )
for i in l:
    if i:
        print(i, end = " ")