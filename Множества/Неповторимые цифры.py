first_list = input()

set_list = set(first_list)


if len(first_list) == len(set_list):
    print('YES')
else:
    print('NO')

a = input()

print('YES' if len(a) == len(set(a)) else 'NO')