s = input().strip()

a, op, b, _, c = s

if a == 'x':
    b = int(b)
    c = int(c)
    print(c - b if op == '+' else c + b)
else:
    a = int(a)
    b = int(b)
    print(a + b if op == '+' else a - b)

