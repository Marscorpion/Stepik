st = input().split()
res = [[]]

for length in range(1, len(st) + 1):
    for start in range(len(st) - length + 1):
        res.append(st[start:start + length])

print(res)