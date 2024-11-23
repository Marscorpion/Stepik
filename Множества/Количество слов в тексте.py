
myset = {w.lower().strip('.,;:-?!') for w in input().split()}

print(len(myset))


text = input().lower().split()

myset = set()
for c in text:
    cleaned_c = c.strip('()*&^%$#@!?/.,:;"')  # Удаляем символы и сохраняем результат
    myset.add(cleaned_c)  # Добавляем обработанное слово в множество

print(len(myset))

import re

text = input()

# Удаляем знаки препинания и разбиваем текст на слова
words = re.findall(r'\b\w+\b', text.lower())

myset = set(words)

print(len(myset))
