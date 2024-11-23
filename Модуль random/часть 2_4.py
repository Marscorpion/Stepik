from random import randrange

lottery = set()

while len(lottery) != 100:
    lottery.add(randrange(1000000, 9999999))

print(*(lottery), sep='\n')

# from random import sample
#
# print(*sample(range(1000000, 10000000), 100), sep='\n')