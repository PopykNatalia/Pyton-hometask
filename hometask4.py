a = int(input("Введіть число a:"))
b = int(input("Введіть число b:"))
c = int(input("Введіть число c:"))
d = str(a)

while a<b:
    print("Дуже погано!")
    a = a+c
    d = d+" "+str(a)
    continue

else:
    print("Неперевершено!")
    print("History:", d)
