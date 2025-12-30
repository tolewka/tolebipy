import math

def circle_area(r):
    return math.pi * r * r

def rectangle_area(a, b):
    return a * b

def triangle_area(a, h):
    return 0.5 * a * h

print("Circle area:", circle_area(5))
print("Rectangle area:", rectangle_area(4, 6))
print("Triangle area:", triangle_area(3, 8))
