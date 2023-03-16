from datetime import datetime
from functools import reduce
from random import randint
import random

#создание рандомного списка из 100000 чисел
def make_a_list():
    l = [ random.randint(1,10) for x in range (1,100001)]
    return l

#сохранение созданного списка в переменной list1
list1 = (make_a_list())

#запись списка в текстовый файл
with open("list_of_100000numbers.txt", "w") as file:
    file.write(str((list1)))
    
#закрытие файла и проверка что он закрыт
f = open('list_of_100000numbers.txt')
f.close()
print(f.closed)   
 
#применение метода reduce для list1
r = reduce(lambda x,y: x+y, list1)
print(r)
