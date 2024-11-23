n = int(input())

num1 = set(input())

for _ in range(n-1):
    num1.intersection_update(input())

print(*sorted(num1))
