def change_fahrenheit(x):
    return x*9/5+32

n = int(input("Enter your centigrade temperature: "))

print(f'{n} Celsius = {change_fahrenheit(n)} Fahrenheit')