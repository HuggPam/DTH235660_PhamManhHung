dai = int(input("Nhap chieu dai: "))
rong = int(input("Nhap chieu rong: "))
for i in range(rong):
    if i == 0 or i == rong - 1:
        print('*' * dai)
    else:
        print('*' + ' ' * (dai - 2) + '*')