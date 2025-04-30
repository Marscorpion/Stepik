# print('YES' if all(any(['5' in input() for _ in range(int(input()))]) for _ in range(int(input()))) else 'NO')

print([any(['5' in input() for _ in range(int(input()))]) for _ in range(int(input()))])