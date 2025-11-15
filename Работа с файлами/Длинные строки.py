# with open('lines.txt', encoding='utf-8') as file:
#     lm = len(max(file.readlines(), key=len))
#     file.seek(0)
#     [print(str.strip()) for str in file.readlines() if len(str) == lm]

with open('lines.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    print(*filter(lambda x: len(x) == max(map(len, lines)), lines), sep='\n')