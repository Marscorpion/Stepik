s = input().split()

d = {}

for word in s:
    d[word] = d.get(word, 0) + 1
    print(d[word], end=' ')





