def divisible_by_digits(n):
    for i in range(1, n + 1):
        digits = str(i)
        ok = True
        for d in digits:
            if d == '0' or i % int(d) != 0:
                ok = False
                break
        if ok:
            print(i, end=" ")

n = int(input("Enter n: "))
divisible_by_digits(n)
