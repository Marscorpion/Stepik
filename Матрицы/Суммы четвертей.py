n = int(input())

matrix = [[int(num) for num in input().split()] for _ in range(n)]

total_upper = 0
total_right = 0
total_bottom = 0
total_left = 0

for i in range(n):
    for j in range(n):
        if i < j and i < n - 1 - j:
            total_upper += matrix[i][j]
        elif i < j and i > n - 1 - j:
            total_right += matrix[i][j]
        elif i > j and i > n - 1 - j:
            total_bottom += matrix[i][j]
        elif i > j and i < n - 1 - j:
            total_left += matrix[i][j]



print('Верхняя четверть:', total_upper)
print('Правая четверть:', total_right)
print('Нижняя четверть:', total_bottom)
print('Левая четверть:', total_left)

# n = int(input())
# mtr = [[int(ch) for ch in input().split()] for _ in range(n)]
#
# print('Верхняя четверть:', sum([mtr[i][j] for i in range(n) for j in range(n) if (i < j and i < n - 1 - j)]))
# print('Правая четверть:', sum([mtr[i][j] for i in range(n) for j in range(n) if (i < j and i > n - 1 - j)]))
# print('Нижняя четверть:', sum([mtr[i][j] for i in range(n) for j in range(n) if (i > j and i > n - 1 - j)]))
# print('Левая четверть:', sum([mtr[i][j] for i in range(n) for j in range(n) if (i > j and i < n - 1 - j)]))


# n = int(input())
# matrix = []
# quadrants = [['Верхняя четверть:', 0],
#              ['Правая четверть:', 0],
#              ['Нижняя четверть:', 0],
#              ['Левая четверть:', 0]]
#
# for _ in range(n):
#     row = [int(i) for i in input().split()]
#     matrix.append(row)
#
# for i in range(n):
#     for j in range(n):
#         if i < j and i + j + 1 < n :
#             quadrants[0][1] += matrix[i][j]
#         elif i < j and i + j + 1 > n:
#             quadrants[1][1] += matrix[i][j]
#         elif i > j and i + j + 1 > n:
#             quadrants[2][1] += matrix[i][j]
#         elif i > j and i + j + 1 < n:
#             quadrants[3][1] += matrix[i][j]
#
# for i in range(4):
#     print(quadrants[i][0], quadrants[i][1])