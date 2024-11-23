word = input() + ' запретил букву '

abc = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

lines = []

for i in abc:
    if i in word:
        word = word + i
        lines.append(word)

        word = word.replace(i, '').replace('  ', ' ')

for i in lines:
    print(i.strip())

word = input() + ' запретил букву'
for i in 'абвгдежзиклмнопрстуфхцчшщъыьэюя':
    if i in word:
        print(word, i)
    word = word.replace(i, '').replace('  ', '')
