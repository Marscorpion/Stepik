import random

n = int(input())

coin = ['Орел', 'Решка']


for _ in range(n):
    f = (random.randint(0, 1))
    print(coin[f])

# print(*[("Орел","Решка")[random.randint(0,1)] for i in range(int(input()))], sep = '\n')