file = open('nums.txt', 'r', encoding='utf-8')

print(sum(map(int, file.read().split())))

file.close()

# txt = open('nums.txt')
# print(sum(map(int, (filter(lambda x: x.strip().isdigit(), txt.readlines())))))
# txt.close()