from random import sample

my_list = [i for i in range(1, 76)]

bingo_list = sample(my_list, 25)

bingo = [[str(bingo_list.pop()).ljust(3) for _ in range(5)] for _ in range(5)]

bingo[2][2] = str(0).ljust(3)

[print(*row, sep='') for row in bingo]

# my_list = [i for i in range(1, 76)]
#
# bingo = sample(my_list, 25)
#
# bingo[12] = 0
#
# while bingo:
#     print(*[str(i).ljust(3) for i in bingo[0: 5]])
#     bingo=bingo[5 ::]




