from functools import reduce
import itertools

beasts = list()

beasts.append({
    "Имя": "Лосяш",
    "Цвет": "Шафрановый",
    "Серии": ["Герой Плутона", "Бабочка", "Долгая рыбалка"]
})

beasts.append({
    "Имя": "Копатыч",
    "Цвет": "Коричневый",
    "Серии": ["Долгая рыбалка", "Кулинария", "Танцор Диско"]
})

#добавление нового персонажа
beasts.append({
    "Имя": "Бараш",
    "Цвет": "Розовый",
    "Серии": ["1 апреля", "Подарок судьбы", "Прощай, Бараш"]
})

#добавление нового ключа и любимых фраз персонажей
beasts[1]["Любимая фраза"]="Укуси меня пчела!"
beasts[0]["Любимая фраза"]="Феноменально!"

#замена цвета Копатыча на Светло-коричневый
beasts[1]["Цвет"]="Светло-коричневый"

#удаление серии "Герой Плутона" из списка серий Лосяша
beasts[0]["Серии"]=["Бабочка", "Долгая рыбалка"]

#cоздание второй структуры, идентичной первой, удаление оттуда записи про Копатыча 
#так чтобы оригинальная структура не поменялась
beasts2 = beasts.copy()
del beasts2[1]

#подсчет количества записанных смешариков
print(f"Количество записанных смешариков = {len(beasts)}")

print(beasts)

print(beasts2)

#запись в файл так чтоб читался русский язык
import json
with open("beasts.json", "w", encoding='utf-8' ) as file:
    file.write(f"{beasts2}")

with open("beasts.txt", "w", encoding='utf-8' ) as file:
    file.write(f"{beasts2}")

beasts3 = beasts.copy()
#функция на поиск по ключу-значению
def getDictsByKeyValue(dicts, key, value):
    dictsres = list(filter(lambda dict: dict[key] == value, dicts))
    return dictsres

#поиск животного по имени
def getBeastByName(beasts, name: str):
    return getDictsByKeyValue(beasts,"Имя", name)[0]

#удаление по имени
def deleteBeastByName(beasts: list, name):
    beasts.remove(getDictsByKeyValue(beasts, "Серии", "Герой Плутона")[0])

#Поиск общих серий
beasts1 = list(filter(lambda x: x in beasts3[0]['Серии'], beasts3[1]['Серии']))

print(beasts1) 

print(beasts3)

#Поиск общих серий2
s1 = set(beasts3[0]['Серии'])
s2 = set(beasts3[1]['Серии'])

print(list( s1 & s2 ))

#Поиск общих серий3
def combunit(ar):    
    p = set(ar[0]) 
    for x in range(1, len(ar)):
        p = p & set(ar[x])
    if (len(p) > 0):
        print(p, ar)
        
def compareSeries(beasts, name1, name2):
    b1 = getBeastByName(beasts3, name1)
    b2 = getBeastByName(beasts3, name2)
    combunit([b1["Серии"], b2["Серии"]])
    
compareSeries(beasts3, "Копатыч", "Лосяш")