import re 

s = input()
print(re.findall('[A-Z][^A-Z]*', s))


"""import re


s = input()
l = re.split('(?=[A-Z])',s )
for i in l:
    if i:
        print(i, end = " ")"""