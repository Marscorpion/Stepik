st = input().split()
n = int(input())

res = [[] for _ in range(n)]


for i in range(len(st)):
    index = i % n
    res[index].append(st[i])

print(res)

# s = input().split()
# n = int(input())
# res = []
# for i in range(n):
#     res.append(s[i::n])
# print(res)
