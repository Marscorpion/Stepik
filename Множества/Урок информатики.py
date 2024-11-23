a, b, c = input().split(), input().split(), input().split()

myset = (set(map(int, a)) & set(map(int, b)))

print(*sorted(myset - set(map(int, c)), reverse=True))
