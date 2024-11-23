n, m = map(int, input().split())

board = [[0 for _ in range(m)] for _ in range(n)]

count = 0

for i in range(n):
    for j in range(m):
        count += 1
        board[i][j] = count

for i in range(n):
    for j in range(m):
        print(str(board[i][j]).ljust(3),  end=' ')
    print()

# n, m = [int(i) for i in input().split()]
# matrix = [[0] * m for _ in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = i * m + j + 1
#
# for i in range(n):
#     for j in range(m):
#         print(str(matrix[i][j]).ljust(3), end=' ')
#     print()