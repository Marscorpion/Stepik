from random import shuffle
# n = int(input())
# pupils = []
#
#
# for _ in range(n):
#     p = input()
#     pupils.append(p)
#
# shuffle(pupils)
#
# for i in range(n):
#     print(f"{pupils[i]} - {pupils[(i + 1) % n]}")

p = [input().split() for i in range(int(input()))]

p2 = p.copy()

for i in range(len(p)):
    while p[i] == p2[i]:
        shuffle(p2)

for i in range(len(p)):
    print(f'{" ".join(p[i])} - {" ".join(p2[i])}')








