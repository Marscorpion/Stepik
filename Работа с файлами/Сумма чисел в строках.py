
with open('numbers.txt') as file:
    lines = [line.strip().split() for line in file.readlines()]
    for l in lines:
         print(sum(map(int, l)))


# with open('numbers.txt') as f:
#     for line in f:
#         print(sum(map(int, line.split())))

# with open('numbers.txt') as f:
#     print(*(sum(map(int, line.split())) for line in f), sep='\n')


