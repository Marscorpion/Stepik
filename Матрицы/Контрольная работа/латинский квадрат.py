n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]

# Функция для проверки, что в строке или столбце содержатся все числа от 1 до n
def check_row_or_column(arr):
    return sorted(arr) == list(range(1, n + 1))

# Проверяем каждую строку
is_latin = all(check_row_or_column(row) for row in matrix)

# Проверяем каждый столбец
if is_latin:
    for j in range(n):
        if not check_row_or_column([matrix[i][j] for i in range(n)]):
            is_latin = False
            break

print("YES" if is_latin else "NO")

