
data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'), (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'), (7029917, 'Massachusetts'), (6910840, 'Tennessee')]

sorted_data = sorted(data, key=lambda word: word[1][-1], reverse=True)

# for c in sorted_data:
#     print(f'{c[1]}: {c[0]}')

# print(*[f'{c[1]}: {c[0]}' for c in sorted_data], sep='\n')

# for pop, city in sorted(data, key=lambda c: c[1][-1], reverse=True):
#     print(f'{city}: {pop}')

[print(f'{s}: {pop}') for s, pop in sorted_data]

# a = sorted(data, key = lambda x: x[1][-1], reverse = True)
# d = dict(a)
# for key, value in d.items():
#     print(value, ': ', key, sep = '')