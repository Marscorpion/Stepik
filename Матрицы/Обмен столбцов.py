n, m = int(input()), int(input())

matrix = [[num for num in input().split()] for _ in range(n)]

col = input().split()

for row in matrix:
        row[int(col[0])], row[int(col[1])] = row[int(col[1])], row[int(col[0])]
        print(*row)

# n, m = int(input()), int(input())
# matrix = [input().split() for _ in range(n)]
# col1, col2 = [int(i) for i in input().split()]
#
# for i in range(n):
#     matrix[i][col1], matrix[i][col2] = matrix[i][col2], matrix[i][col1]
#
# for row in matrix:
#     print(*row)


