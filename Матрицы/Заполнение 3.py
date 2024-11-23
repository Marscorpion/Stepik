n = int(input())

board = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j or j == n - i - 1:
            board[i][j] = 1

for row in board:
    print(*row)

# n = int(input())
#
# res = [[1 if i == j or i == n - j - 1 else 0 for j in range(n)] for i in range(n)]
#
# for x in res:
#     print(*x)