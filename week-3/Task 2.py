def array_sum_and_mean(arr):
    s = sum(arr)
    mean = s / len(arr)
    return s, mean

arrays = [
    [1, 2, 3, 4],
    [5, 10, 15],
    [7, 14, 21, 28]
]

for i, arr in enumerate(arrays, 1):
    s, m = array_sum_and_mean(arr)
    print(f"Array {i}: sum = {s}, mean = {m}")

