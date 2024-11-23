
word_1 = {}
word_2 = {}

for c in input():
    word_1[c] = word_1.get(c, 0) + 1

for c in input():
    word_2[c] = word_2.get(c, 0) + 1


print("YES" if word_1 == word_2 else "NO")

dcts = ({}, {})
for d in dcts:
    for c in input().lower():
        d[c] = d.get(c, 0) + 1

print(('NO', 'YES')[dcts[0] == dcts[1]])