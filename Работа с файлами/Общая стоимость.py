
file = open('prices.txt', 'r', encoding='utf-8')

prices = [line.strip().split() for line in file]

print(sum(int(line[-1]) * int(line[-2]) for line in prices))

file.close()

# from functools import reduce
#
# file = open("prices.txt", encoding="utf-8")
# prods = [ x.split() for x in file.readlines()]
# amount = reduce(lambda a,b:  a + int(b[1]) * int(b[2]), prods, 0)
# print(amount)
# file.close()



