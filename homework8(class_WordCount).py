from collections import Counter
from time import perf_counter


class word_count():
    text = input("Введите свой текст здесь:  ")
start_time = perf_counter()   
res1 =''.join( x for x in word_count.text if x.isalpha() or x == ' ' ).lower()
res_final = list(filter( lambda x : x != '', res1.split(" ")))
print(f"{res_final}\n")
print(f"{Counter(res_final)}\n")
print(f"Количество слов в тексте = {len(res_final)}\n")
end_time = perf_counter()
print(f'Время на выполнение кода: {end_time-start_time} секунд')
