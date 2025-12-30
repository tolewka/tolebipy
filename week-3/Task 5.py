def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def subtract_fractions(A, B, C, D):
    num = A * D - B * C
    den = B * D
    g = gcd(abs(num), den)
    return num // g, den // g

n, d = subtract_fractions(5, 6, 1, 3)
print(f"Result: {n}/{d}")
