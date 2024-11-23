from random import randint

lottery = set()

while len(lottery) != 7:
    lottery.add(randint(1, 49))

print(*sorted(lottery))

