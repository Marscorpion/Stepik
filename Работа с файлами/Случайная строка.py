import random
file = open("lines.txt", 'r', encoding='utf-8')

print(*random.sample(file.readlines(), 1))

file.close()