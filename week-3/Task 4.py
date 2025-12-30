def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def divide_fractions(A, B, C, D):
    num = A * D
    den = B * C
    g = gcd(num, den)
    return num // g, den // g

n, d = divide_fractions(2, 3, 4, 5)
print(f"Result: {n}/{d}")
