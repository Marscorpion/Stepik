
a = input().split()

d = int(a[-1])

for i in a[-2::-1]:
    d = {int(i):d}

print(d)

# a = [100, 55, 77, 55, 89]
#
# result_dict = {}
# count = -3
# for i in range(len(a)-1):
#     if len(result_dict) == 0:
#         result_dict = {a[-2]: a[-1]}
#         print(result_dict)
#     else:
#         result_dict = {a[count]: result_dict}
#         print(result_dict)
#         count -= 1
# print(result_dict)