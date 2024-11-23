
s = [c.strip('.,!?:;-') for c in input().lower().split()]

words = {}
for word in s:
    words[word] = words.get(word, 0) + 1

print(min([key for key, value in words.items() if value == min(words.values())]))


# dct = {}
# lst = [word.strip('.,!?:;-') for word in input().lower().split()]
# for word in lst:
#     dct[word] = dct.get(word, 0) + 1
# lst = [(value, key) for key, value in dct.items()]
# lst.sort()
# print(lst[0][1])