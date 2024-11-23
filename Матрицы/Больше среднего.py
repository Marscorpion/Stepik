n = int(input())

matrix = [[int(num) for num in input().split()] for _ in range(n)]


for row in matrix:
    count = 0
    for i in row:
        if i > sum(row) / n:
            count += 1
    print(count)

# n = int(input())
# matrix = [list(map(int, input().split())) for __ in range(n)]


# for i in range(n):
#     total = 0
#     for j in range(n):
#         if matrix[i][j] > sum(matrix[i]) / len(matrix[i]):
#             total += 1
#     print(total)
