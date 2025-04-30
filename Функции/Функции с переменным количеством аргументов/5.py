def print_products(*args):
    prod = [i for i in args if type(i) is str and i]
    if prod:
        for j in range(len(prod)):
            print(f'{j+1}) {prod[j]}')
    else:
        print("Нет продуктов")

# def print_products(*args):
#     cnt = 0
#     for e in args:
#         if type(e) == str and e:
#             cnt += 1
#             print(f'{cnt}) {e}')
#     if cnt == 0:
#         print('Нет продуктов')

print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
print_products([4], {}, 1, 2, {'Beegeek'}, '')