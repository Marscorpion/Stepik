

result = [[int(input().split()[1]) for _ in range(int(input()))] for _ in range(int(input()))]

# print(result)


# print('YES' if all([any([5 in i for i in result])]) else 'NO')

print(any(map(lambda i: 5 in i, result)))




# print('YES' if all(any(['5' in input() for _ in range(int(input()))]) for _ in range(int(input()))) else 'NO')