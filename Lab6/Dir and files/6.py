path = "D:\Educational materials\Programming principles 2\Python\PP2_21B030956\Lab6\Dir and files\Forder for 26 file"
for i in range(65, 91):
    k = chr(i) + ".txt"
    s = f"\{k}"
    with open(path + s, "w") as fil:
        fil.write("")

        