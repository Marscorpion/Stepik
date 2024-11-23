n = int(input())
res = [input().split() for _ in range(n)]

coun = {}

for i in res:
    coun[i[0]] = coun.get(i[0], []) + i[1 ::]

m = int(input())

for c in range(m):
    c = input()
    for key, value in coun.items():
        for i in value:
            if i == c:
                 print(key)

