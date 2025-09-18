
import random
# Sinh thử 10 số ngẫu nhiên với randrange(0, 100)
for _ in range(10):
    print(random.randrange(0, 100))

# Kiểm tra các giá trị cụ thể có thể xuất hiện không
def check_value(val):
    if 0 <= val < 100 and isinstance(val, int):
        print(f"{val} có thể xuất hiện.")
    else:
        print(f"{val} không thể xuất hiện.")

values = [4.5, 34, -1, 100, 0, 99]
for v in values:
    check_value(v)