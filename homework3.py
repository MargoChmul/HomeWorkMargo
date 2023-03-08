from random import randint
import random
#функция на создание рандомного списка длиной от 4 до 12 элементов, содержащего числа от 1 до 66
def make_a_list():
    l = [ random.randint(1,66) for x in range(randint(4,12)) ]
    return l
#создание рандомного списка списков длиной 18000
l1=[]
for i in range (18000):
    l1.append(make_a_list())
print(l1)
#проверка длины списка
print(f"Длина списка = {len(l1)} рандомных списков")
    