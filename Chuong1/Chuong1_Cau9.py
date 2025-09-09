dai = int(input("Nhap chieu dai: "))
rong = int(input("Nhap chieu rong: "))

if dai == rong:
    print("Day la hinh vuong")
else:
    for i in range(rong):
        print('* ' * dai)