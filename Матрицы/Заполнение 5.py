n, m = map(int, input().split())

board = [[i  for i in range(1, m+1)] for _ in range(n)]

counter = 0

for row in board:
    for i in range(counter):
        row.append(row.pop(0))
    counter += 1
    print(*row)

# n, m = [int(i) for i in input().split()]
# matrix = [[0] * m for _ in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = (i + j) % m + 1
#
# for i in range(n):
#     for j in range(m):
#         print(str(matrix[i][j]).ljust(3), end=' ')
#     print()

# n, m = map(int, input().split())
# a = [i for i in range(1, m+1)]
# for i in range(n):
#     print(*a)
#     a = a[1:] + a[:1]