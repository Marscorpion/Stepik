n = int(input())

# print(*[[i for i in range(1, n+1)] for i in range(n)], sep='\n')

for _ in range(n):
    my_list = []

    for i in range(1, n+1):
        my_list.append(i)
    print(my_list)






