from collections import Counter

class word_count():
    def __init__(self) -> None:
        self.text = input("Введите свой текст здесь:  ")
        self.res1 =''.join( x for x in self.text if x.isalpha() or x == ' ' ).lower()
        self.res_final = list(filter( lambda x : x != '', self.res1.split(" ")))
        print(f"{self.res_final}\n")
        print(f"{Counter(self.res_final)}\n")
        print(f"Количество слов в тексте = {len(self.res_final)}\n")
        
word_count()
