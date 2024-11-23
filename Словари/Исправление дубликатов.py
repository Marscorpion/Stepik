
s = input().split()

count = {}

result = []
for word in s:
    if word in count:
        count[word] += 1
        result.append(f'{word}_{count[word] - 1}')
    else:
        count[word] = 1
        result.append(word)

# lst = input().split()
# res = {}
# for c in lst:
#     if c in res:
#         print(f'{c}_{res[c]}', end=' ')
#     else:
#         print(c, end=' ')
#     res[c] = res.get(c, 0) + 1

print(*result)

