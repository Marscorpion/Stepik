st = input().split()

n = int(input())

res = []

for el in st:
    if res and len(res[-1]) < n:
        res[-1].append(el)
    else:
        res.append([el])

print(res)


# st = input().split()
# n = int(input())
#
# packed_list = []
#
# sub = []
#
#
# for i in st:
#     if len(sub) < n:
#         sub.append(i)
#     else:
#         packed_list.append(sub)
#         sub = [i]

if sub:
    packed_list.append(sub)

print(packed_list)
