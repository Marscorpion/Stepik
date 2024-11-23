a, b = input(), input()

if a == b:
    print('ничья')

win = ['нб','бк','кя','яС','Сн','ня','яб','бС','Ск','кн']

for c in win:
    if a[0] == c[0] and b[0] == c[1]:
        print('Тимур')

    elif a[0] == c[1] and b[0] == c[0]:
        print('Руслан')

options = ["камень", "ящерица", "Спок", "ножницы", "бумага"]
results = ["ничья", "Руслан", "Тимур", "Руслан", "Тимур"]

timur_move = input()
ruslan_move = input()

case = options.index(timur_move) - options.index(ruslan_move)
res = results[case]

"камень", "ножницы", "бумага", "ящерица", "Спок"
m = {"камень": ["ножницы", "ящерица"],
    "ножницы": ["бумага", "ящерица"],
    "бумага": ["камень", "Спок"],
    "ящерица": ["Спок", "бумага"],
    "Спок": ["камень", "ножницы"]}
t, r = input(), input()
if r == t:
    print("ничья")
elif r in m[t]:
    print("Тимур")
else:
    print("Руслан")