a, b, c = (set(int(i) for i in input().split()) for i in range(3))

print(*sorted((a | b | c) - (a & b & c)))