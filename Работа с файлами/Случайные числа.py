from random import *
# a = list(range(111, 778, 1))

with open('random.txt', 'w', encoding='utf-8') as file:
       # print(*(sample(a, 25)), sep='\n', file = file)

       print(*[randint(111, 777) for _ in range(25)], sep='\n', file=file)



