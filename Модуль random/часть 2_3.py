from random import shuffle

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

# for i in matrix:
#     shuffle(i)

[shuffle(i) for i in matrix]

shuffle(matrix)

print(*matrix, sep='\n')