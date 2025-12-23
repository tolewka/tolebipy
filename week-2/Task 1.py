s = input().strip()

count = 0

for i in range(len(s) - 3):
    if s[i:i+4] == ">-->":
        count += 1
    elif s[i:i+4] == "<--<":
        count += 1

print(count)

