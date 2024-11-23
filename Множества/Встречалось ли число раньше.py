n = [int(i) for i in input().split()]
set_n = set()


for i in n:
    if i in set_n:
        print('YES')
    else:
        print("NO")
    set_n.add(i)






