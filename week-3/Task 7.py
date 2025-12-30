def right_triangle_area(a, b):
    return 0.5 * a * b

def rectangle_area(a, b):
    return a * b

X = float(input("X: "))
Y = float(input("Y: "))
Z = float(input("Z: "))
T = float(input("T: "))

area = right_triangle_area(X, Y) + rectangle_area(Z, T)
print("Area of quadrilateral:", area)
