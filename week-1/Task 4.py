N = int(input())
if N >= 1:
    sum_numbers = N * (N + 1) // 2
else:
    sum_numbers = N * (N - 1) // 2 + 1
print(sum_numbers)
