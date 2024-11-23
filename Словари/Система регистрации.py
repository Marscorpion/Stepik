# n = int(input())
#
# database = {}
#
# for _ in range(n):
#     log = input()
#     if log in database:
#         database[log] = database.get(log, 0) +1
#         database[f'{log}{database[log]}'] = 0
#         print(log, database[log], sep='')
#     else:
#         database[log] = 0
#         print('OK')

d = {}

for _ in  range(int(input())):
    log = input()
    z = d.get(log, 0)
    print(f'{log}{z}' if z else 'OK')
    d[log] = z + 1
    if z != 0:
        d[f'{log}{z}'] = 0

print(d)