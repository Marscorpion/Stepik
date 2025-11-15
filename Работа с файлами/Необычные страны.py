# with open('population.txt') as file:
#     countries = [line.strip().split('\t') for line in file.readlines()]
#     for c in countries:
#         if int(c[1]) > 500000 and c[0][0] == 'G':
#             print(c[0])


with open('population.txt') as f:
    for line in f:
        n, p = line.split('\t')
        if n.startswith('G') and int(p) > 500000:
            print(n)






