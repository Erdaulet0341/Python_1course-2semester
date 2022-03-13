import re

input_file_name = "roww.txt"
result_file_name = "SWK.txt"

input_file = open(input_file_name, mode = 'r', encoding="Latin-1")
result_file = open(result_file_name, mode = 'w', encoding="Latin-1")

mytext = input_file.read()
patterns = "SWK\d{6}"
res = re.findall(patterns, mytext)
result_file.write(str(res))
