n, m = map(int, input().split())

board = [[0 for _ in range(m)] for _ in range(n)]


for i in range(n):
    for j in range(m):
        board[i][j] = i + j * n + 1




for i in range(n):
    for j in range(m):
        print(str(board[i][j]).ljust(3),  end=' ')
    print()

# row, col = input().split()
#
# lst = [[0 for x in range(int(col))] for _ in range(int(row))]
# counter = 1
#
# for i in range(int(col)):
#     for j in range(int(row)):
#         lst[j][i] = counter
#         counter += 1
# for r in lst:
#     print(*r)

# n, m = [int(k) for k in input().split()]
# matrix = [[str(i + j * n).rjust(3) for j in range(m)] for i in range(1, n + 1)]
# for row in matrix:
#     print(*row)