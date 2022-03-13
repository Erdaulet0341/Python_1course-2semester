import re

input_file_name = "roww.txt"
result_file_name = "Стоимость.txt"

input_file = open(input_file_name, mode = 'r', encoding="Latin-1")
result_file = open(result_file_name, mode = 'w', encoding="Latin-1")

mytext = input_file.read()
patterns = "\d+,0{3}\sx\s\d+,00"
res = re.findall(patterns, mytext)
for i in res:
    result_file.write(i + "\n")
