import re

word = input()
c = ''
for i in range(len(word)):
    if word[i] == '_':
        c = word[i+1]
        c = c.upper()

k = re.sub('[_][a-z]', c, word)
print(k)