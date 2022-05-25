a = int(input())
b = int(input())
c = int(input())
if a > b:
    print('Війна розпочалася')
elif a == b:
    print('Сили сторін рівні')
else:
    if b > c:
        print('МИ ПЕРЕМОГЛИ!')
    else :
        print('Орки розбомбили 2 населені пункти, але наше ЗСУ розбомбило орків')