# with open("data.txt", 'r', encoding='utf-8') as file:
#     print(*map(str.strip, file.readlines()[:: -1]), sep='\n')

with open('data.txt', encoding='utf-8') as file:
    print(*file.readlines()[::-1], sep='')