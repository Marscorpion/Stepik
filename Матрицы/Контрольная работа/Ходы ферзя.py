board = [['.'] * 8 for _ in range(8)]

coords = input()
x = ord(coords[0]) - 97
y = 8 - int(coords[1])


for i in range(len(board)):
    for j in range(len(board[i])):
        if i == y or j == x:
            board[i][j] = '*'
        elif  abs(x - j) == abs(y - i):
            board[i][j] = '*'

board[y][x] = "Q"

for i in range(len(board)):
    for j in range(len(board[i])):
        print(board[i][j], end=' ')
    print()