import datetime
day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))
try:
    d = datetime.date(year, month, day)
    next_day = d + datetime.timedelta(days=1)
    print("Ngày kế tiếp:", next_day.strftime("%d/%m/%Y"))
except ValueError:
    print("Ngày không hợp lệ!")