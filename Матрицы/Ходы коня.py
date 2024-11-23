board = [['.'] * 8 for _ in range(8)]

coords = input()
x = ord(coords[0]) - 97  # Переводим букву в индекс столбца
y = 8 - int(coords[1])   # Переводим номер строки в индекс

# Размещаем коня на доске
board[y][x] = "N"

for i in range(len(board)):
    for j in range(len(board[i])):
        if (i == y + 2 or i == y - 2) and (j == x - 1 or j == x + 1) and i >=0 and j >= 0:
            board[i][j] = '*'
        elif  (i == y + 1 or i == y - 1) and (j == x - 2 or j == x + 2) and i >=0 and j >= 0:
            board[i][j] = '*'
# Выводим доску
for i in range(len(board)):
    for j in range(len(board[i])):
        print(board[i][j], end=' ')
    print()

# x, y = input()
# n = 8
# board = [['.'] * n for _ in range(n)]
# x = ord(x) - 97
# y = n - int(y)
# board[y][x] = 'N'
#
# for i in range(n):
#     for j in range(n):
#         if abs(y - i) * abs(x - j) == 2:
#             board[i][j] = '*'
#
# for row in board:
#     print(*row)