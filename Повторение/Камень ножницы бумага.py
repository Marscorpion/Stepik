a, b = input(), input()

if a == 'камень' and b =='ножницы' or a =='ножницы' and b =='бумага' or a == 'бумага' and b =='камень':
    print('Тимур')
elif a == 'камень' and b =='бумага' or a == 'бумага' and b =='ножницы' or a == 'ножницы' and b =='камень':
    print('Руслан')
elif a == b:
    print('ничья')
else:
    print('ничья')

# options = ["камень", "ножницы", "бумага"]
# results = ["ничья", "Руслан", "Тимур"]
#
# timur_move = input()
# ruslan_move = input()
#
# case = options.index(timur_move) - options.index(ruslan_move)
# res = results[case]
#
# print(res)