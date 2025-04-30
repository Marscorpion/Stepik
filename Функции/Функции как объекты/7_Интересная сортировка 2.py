numbers = sorted([int(i) for i in input().split()])

def summ(num):
    num = [int(i) for i in str(num)]
    return sum(num)

print(*sorted(numbers, key=summ))

# numbers = input().split()
#
# def summ(num):
#     digits_sum = sum(int(i) for i in num)
#     return digits_sum, int(num)  # Сначала сортировка по сумме цифр, затем по самому числу
#
# print(*sorted(numbers, key=summ))