sen_1, sen_2 = {}, {}

for c in input().lower():
    if c.isalpha():
        sen_1[c] = sen_1.get(c, 0) + 1

for c in input().lower():
    if c.isalpha():
        sen_2[c] = sen_2.get(c, 0) + 1


print("YES" if sen_1 == sen_2 else "NO")

