import math

def S(x, n):
    result = 0
    for k in range(n + 1):
        result += (x ** (2 * k + 1)) / math.factorial(2 * k + 1)
    return result

# Nhập giá trị x và n từ bàn phím
x = float(input("Nhập x: "))
n = int(input("Nhập n: "))
print("Giá trị biểu thức S(x, n) là:", S(x, n))