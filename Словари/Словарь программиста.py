n = int(input())

dic = {}

for _ in range(n):
    key, value=input().split(': ')
    dic[key.lower()] = value

m = int(input())
for c in range(m):
    c = input().lower()
    if c in dic:
        print(dic[c])
    else:
        print("Не найдено")

# for _ in range(int(input())):
#     print(dic.get(input().lower(), 'Не найдено'))


# a =  [(input().split(':')) for i in range(int(input()))]
#
# b = {i[0].lower(): i[1].strip() for i in a}
#
# for j in [input().lower() for j in range(int(input()))]:
#     print(b.get(j, "Не найдено"))