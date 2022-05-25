def hometask1():
    (print('hello world!'))
hometask1()

def hometask2(a = input('введіть дані a'), b = input('введіть дані b'), c = input('введіть дані c')):
    (print(a+' '+b+' '+c+'!'))
hometask2()

def hometask3(  a = int(input()),b = int(input()),c = int(input())):

    if a > b:
        print('Війна розпочалася')
    elif a == b:
        print('Сили сторін рівні')
    else:
        if b > c:
            print('МИ ПЕРЕМОГЛИ!')
        else:
            print('Орки розбомбили 2 населені пункти, але наше ЗСУ розбомбило орків')
hometask3()

def hometask4 (a = int(input("Введіть число a:")),b = int(input("Введіть число b:")),c = int(input("Введіть число c:"))):
    d = str(a)
    while a < b:
        print("Дуже погано!")
        a = a + c
        d = d + " " + str(a)
        continue
    else:
        print("Неперевершено!")
        print("History:", d)
hometask4()