def change_ounces(x):
    return n*28.3495231

n = int(input("Enter your grams: "))

print(f"{n} grams = {change_ounces(n)} ounces")