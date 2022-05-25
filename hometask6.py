from random import randint


def randomlist(a = int(input("Значення початку діапазону: ")), b = int(input("Значення кінця діапазону: ")), c = int(input("Кількість елементів у списку "))):
    d = [randint(a, b) for i in range(c)]
    print(d)

randomlist()

