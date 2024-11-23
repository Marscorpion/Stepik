result = {}

for i in range(1, 16):
     result.setdefault(i, i ** 2)

print(result)

result = {}
for i in range(1, 16):
    result[i] = i * i