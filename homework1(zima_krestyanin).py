phrase = "зима 32нео крестьянин торжествуя 42на на"
#перевод строки в список и одновременное избавление от цифр
phrase_new1 = list(''.join( letter for letter in phrase if letter.isalpha() or letter == ' ' ))
#срез ненужных символов и слов + начало строки с загланой буквы + возврат обратно в тип строка
phrase_new2 = ''.join(phrase_new1[:4] + phrase_new1[8:30]).capitalize()
#вывод на печать с добавлением запятой после первого слова
print(f"{phrase_new2[:4]},{phrase_new2[5:]}")

