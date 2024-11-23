import random

length = int(input())

# password = []
# for _ in range(length):
#     password.append(chr((random.randint(65, 90))))
#     password.append(chr((random.randint(97, 122))))
#     print(password[random.randrange(0, len(password))], end='')

for i in range(length):
    r = {0: random.randrange(65, 91), 1: random.randrange(97, 123)}
    print(chr(r[random.randint(0, 1)]), end='')


