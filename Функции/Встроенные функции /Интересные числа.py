a, b = int(input()), int(input())
numbers = []

for i in range(a, b+1):
    if '0' not in str(i):
        numbers.append(i)

# result = []

for j in (numbers):
    if all(j % int(c) ==0 for c in str(j)):
        # result.append(j)
        print(j, end=' ')

# print(*result)

# for i in range(a, b + 1):
#     # создаем кортеж со всеми цифрами числа
#     digits = tuple(map(int, str(i)))
#
#     # проверяем, что число не содержит 0 и делится на все свои цифры
#     if 0 not in digits and all(map(lambda cur_digit: i % cur_digit == 0, digits)):
#         print(i, end=" ")

# for i in range(a, b + 1):
#     # создаем кортеж со всеми цифрами числа
#     digits = tuple(map(int, str(i)))
#
#     # проверяем, что число не содержит 0 и делится на все свои цифры
#     if 0 not in digits and all(i % c == 0  for c in digits):
#         print(i, end=" ")












