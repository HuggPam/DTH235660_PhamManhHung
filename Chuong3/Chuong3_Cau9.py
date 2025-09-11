thang = int(input("Nhập vào số tháng (1-12): "))

if 1 <= thang <= 3:
    quy = 1
elif 4 <= thang <= 6:
    quy = 2
elif 7 <= thang <= 9:
    quy = 3
elif 10 <= thang <= 12:
    quy = 4
else:
    print("Tháng không hợp lệ!")
    exit()

print(f"Tháng {thang} thuộc quý {quy} trong năm.")