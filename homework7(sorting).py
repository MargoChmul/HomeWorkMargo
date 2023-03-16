from itertools import groupby
from datetime import datetime
from time import perf_counter

new_gym_klients = [{"number_of_month": 1, "month": "january", "name": "Ivan Ivanov", "age": 19},
               {"number_of_month": 1, "month": "january", "name": "Ivan Petrov", "age": 34},
               {"number_of_month": 2, "month": "february", "name": "Anna Zak", "age": 24},
               {"number_of_month": 3, "month": "march", "name": "Adolf Hitler", "age": 46},
               {"number_of_month": 3, "month": "march", "name": "Josef Stalin", "age": 56},
               {"number_of_month": 4, "month": "april", "name": "Noah Kirel", "age":22},
               {"number_of_month": 5, "month": "mai", "name": "Vika Levinsky", "age": 36},
               {"number_of_month": 5, "month": "mai", "name": "Karina Ivanov", "age": 18},
               {"number_of_month": 6, "month": "juny", "name": "Ran Siren", "age": 76},
               {"number_of_month": 7, "month": "july", "name": "Sonya Loren", "age": 62},
               {"number_of_month": 8, "month": "august", "name": "Ivan Ivanov", "age": 19},
               {"number_of_month": 8, "month": "august", "name": "Vilena Starv", "age": 38},
               {"number_of_month": 9, "month": "september", "name": "Margarita Chmul", "age": 29},
               {"number_of_month": 10, "month": "oktober", "name": "Vladimir Zelensky", "age": 42},
               {"number_of_month": 10, "month": "oktober", "name": "Valentina Dudik", "age": 39},
               {"number_of_month": 11, "month": "november", "name": "Nina Sartik", "age": 26},
               {"number_of_month": 12,"month": "december", "name": "Tamir Ransky", "age": 37}]


#сортировка по имени месяца
print("\nCортировка по имени месяца\n")


start_time = perf_counter()
new_gym_klients.sort(key=lambda x: x["month"])
result = []
for x, y  in groupby(new_gym_klients, key=lambda x: x["month"]):
    print(x, list(y))
end_time = perf_counter()
print(f'Время на выполнение кода: {end_time-start_time} секунд\n')


print("\nCортировка по номеру месяца\n")    
#сортировка по номеру месяца
start_time = perf_counter()    
new_gym_klients.sort(key=lambda x: x["number_of_month"])   
result = []
for x, y  in groupby(new_gym_klients, key=lambda x: x["number_of_month"]):
    print(x, list(y))
end_time = perf_counter()
print(f'Время на выполнение кода: {end_time-start_time} секунд\n')


print("\nCортировка по возрасту\n")  
#сортировка по возрасту
start_time = perf_counter()    
new_gym_klients.sort(key=lambda x: x["age"])   
result = []
for x, y  in groupby(new_gym_klients, key=lambda x: x["age"]):
    print(x, list(y))
end_time = perf_counter()
print(f'Время на выполнение кода: {end_time-start_time} секунд\n')  

     
print("\nCортировка по имени\n")  
#сортировка по имени
start_time = perf_counter()  
new_gym_klients.sort(key=lambda x: x["name"])   
result = []
for x, y  in groupby(new_gym_klients, key=lambda x: x["name"]):
    print(x, list(y))
end_time = perf_counter()
print(f'Время на выполнение кода: {end_time-start_time} секунд\n')


