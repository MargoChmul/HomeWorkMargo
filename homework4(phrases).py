text = "Привет, мир!\nЯ учу пайтон.\n"
text2 = "Добавляю запись и закрываю файл для изменений."
#создание файлов в разных кодировках
with open("phrases.txt", "w", encoding='utf-8' ) as file:
    file.write(text)
    
with open("phrases2.txt", "w", encoding='cp1251' ) as file:
    file.write(text)
    
with open("phrases3.txt", "w", encoding='cp866' ) as file:
    file.write(text)
    
with open("phrases4.txt", "w", encoding='koi8-r' ) as file:
    file.write(text)
#добавление текста в файл    
with open("phrases2.txt", "a") as file:
    file.write(text2)
#закрытие файла    
f = open('phrases2.txt')
f.close()
print(f.closed)