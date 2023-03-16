#импорт текста о Шерлоке сразу в виде строки
from file_sherlok_holmes import file_sherlok
#избавление от цифр и знаков пунктуации
text = ''.join( x for x in file_sherlok if x.isalpha() or x == ' ' ).lower()
#превращение текста в список слов с разбитием по пробелу
text_final = list(filter( lambda x : x != '', text.split(" ")))
#вывод на печать повторяющихся слов 
from collections import Counter
print(Counter(text_final))
#подсчет количества слов в тексте
print(f"Количество слов в тексте = {len(text_final)}")


#эффекивность и время выполнения кода
from datetime import datetime
from time import perf_counter

start_time = perf_counter()
print(datetime.now())

from file_sherlok_holmes import file_sherlok
text = ''.join( x for x in file_sherlok if x.isalpha() or x == ' ' ).lower()
text_final = list(filter( lambda x : x != '', text.split(" ")))
from collections import Counter
print(Counter(text_final))
print(f"Количество слов в тексте = {len(text_final)}")

end_time = perf_counter()
print(f'Время на выполнение кода: {end_time-start_time: 0.2f} секунд')
print(datetime.now())