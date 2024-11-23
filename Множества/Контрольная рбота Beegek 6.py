m = int(input())

n = int(input())
first_set = set(input() for _ in range(n))

for _ in range(m - 1):
    n = int(input())
    current_set = set(input() for _ in range(n))
    first_set.intersection_update(current_set)

for name in sorted(first_set):
    print(name)