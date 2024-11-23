n = int(input())

dic = {}

for _ in range(n):
    key, value=input().split()
    dic[key] = value

a = input()

for key, value in dic.items():
    if value == a:
        print(key)
    elif key == a:
        print(value)