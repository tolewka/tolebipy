import math

def hypotenuse(a, b):
    return math.sqrt(a*a + b*b)

h1 = hypotenuse(3, 4)
h2 = hypotenuse(6, 8)

print("Hypotenuse 1:", h1)
print("Hypotenuse 2:", h2)

if h1 > h2:
    print("First hypotenuse is greater")
elif h1 < h2:
    print("Second hypotenuse is greater")
else:
    print("Hypotenuses are equal")

