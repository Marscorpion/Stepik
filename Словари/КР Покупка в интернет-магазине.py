n = int(input())

s = {}

for _ in range(n):
    name, goods, quantity = input().split()
    quantity = int(quantity)
    if name in s:
        if goods in s[name]:
            s[name][goods] += quantity
        else:
            s[name][goods] = quantity
    else:
        s[name] = {goods: quantity}

for name in sorted(s):
    print(name + ':')
    for goods in sorted(s[name]):
        print(goods, s[name][goods])