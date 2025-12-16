A = 12.34

int_part = int(A)
frac_part = A - int_part

frac_as_int = int(frac_part * 100)
int_as_frac = int_part / 100

new_A = frac_as_int + int_as_frac
print(new_A)  # 34.12

