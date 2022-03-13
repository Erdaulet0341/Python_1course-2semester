import re

s = input()
print(re.sub("(.)([A-Z][a-z])+",r'\1_\2', s).lower())




"""import re
 
def change_case(s):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
     
s = input()
print(change_case(s))"""
