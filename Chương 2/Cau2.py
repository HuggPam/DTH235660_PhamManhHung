t=int(input("Nhập số giây:"))
h=(t//3600)%24
m=(t%3600)//60
s=(t%3600)%60
print(h,":",m,":",s)
