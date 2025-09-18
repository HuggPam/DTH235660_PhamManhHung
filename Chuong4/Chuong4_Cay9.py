import math

n = int(input("Nhập n: "))
s = 0
for _ in range(n):
    s = math.sqrt(2 + s)
print(f"Giá trị S({n}) = {s}")