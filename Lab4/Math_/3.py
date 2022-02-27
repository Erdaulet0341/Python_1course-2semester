import math

n = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))

p = n*l
a = l/(2*math.tan(math.radians(180/n)))

print(f'The area of the polygeon is: {int(p*a/2)}')