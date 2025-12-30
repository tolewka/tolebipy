def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

A = int(input("Enter A: "))
B = int(input("Enter B: "))

print("GCD:", gcd(A, B))
print("LCM:", lcm(A, B))
