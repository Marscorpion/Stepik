dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = {}

result.update(dict2)

for  key in dict1.keys():
    for k in dict2.keys():
        if key == k:
            dict1[key] += dict2[key]

result.update(dict1)

# result = dict1.copy()
#
# for key, value in dict2.items():
#     result[key] = result.get(key, 0) + value



print(result)