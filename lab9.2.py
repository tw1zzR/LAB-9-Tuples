
d = int(input("Введіть цілий дільник числа: "))
A = set(range(1,251))

divisors = {i for i in A if i % d == 0}
A.difference_update(divisors)

print(f"\nМножина A після видалення дільників числа {d}: {A}")