n, m = map(int, input().split())

board = [['.' for _ in range(m)] for _ in range(n)]


for i in range(n):
    for j in range(m):
         if (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0):
            board[i][j] = '*'

for row in board:
    print(*row)