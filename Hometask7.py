from random import randint
a = int(input("Значення початку діапазону: "))
b = int(input("Значення кінця діапазону: "))
c = int(input("Кількість елементів у списку "))

Mylist = [randint(a, b) for i in range(c)]
print(Mylist)

item = int(input("Оберіть необхідне число з списку: "))

index = Mylist.index(item)
print("The index of", item, "in the list is", index)
