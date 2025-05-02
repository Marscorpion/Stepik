result = [[int(input().split()[1]) for _ in range(int(input()))] for _ in range(int(input()))]


print('YES' if all(map(lambda x: 5 in x, result)) else 'NO')

# print(('NO', 'YES')[all([any(['5' in input() for _ in 'k'*int(input())]) for _ in 'n'*int(input())])])

# n = int(input())
# students = []
# for _ in range(n):
#     m = int(input())
#     temp = []
#     for _ in range(m):
#         surname, mark = input().split()
#         temp.append((surname, int(mark)))
#     students.append(temp)
#
# result = all(map(lambda x: any(map(lambda y: y[1] == 5, x)), students))
# print('YES' if result else 'NO')

