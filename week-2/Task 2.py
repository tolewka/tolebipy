a = input().strip()
b = input().strip()

n = len(a)
m = len(b)

bb = b + b
count = 0

for i in range(n - m + 1):
    sub = a[i:i + m]
    if sub in bb:
        count += 1

print(count)
