a, b, c = (set(int(i) for i in input().split()) for i in range(3))

d = {i for i in range(11)}

print(*sorted(d.difference(a, b, c)))

# print(*sorted(set(range(11)) - (a | b | c)))