score = {1: ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'],
       2: ['D', 'G'],
       3: ['B', 'C', 'M', 'P'],
       4: ['F', 'H', 'V', 'W', 'Y'],
       5: 'K',
       8: ['J', 'X'],
       10: ['Q', 'Z']}

word = input()
total = 0

for k, v in score.items():
    for i in word:
        if i in v:
            total += k

print(total)

# print(sum([k for i in input() for k, v in score.items() if i in v]))