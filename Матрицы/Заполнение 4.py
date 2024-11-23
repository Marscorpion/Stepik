n = int(input())

board = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j or j == n - i - 1:
            board[i][j] = 1
        elif (i < j and i < n-1 -j) or (i > j and i > n-1 -j):
            board[i][j] = 1

# for i in range(n):
#     for j in range(n):
#         if (i <= j and i + j + 1 <= n) or (i >= j and i + j + 1 >= n):
#             board[i][j] = 1

for row in board:
    print(*row)