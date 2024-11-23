n = int(input())

matrix = [input().split() for _ in range(n)]

matrix = matrix[-1 :: -1]
# matrix.reverse()

for row in matrix:
    print(*row)


