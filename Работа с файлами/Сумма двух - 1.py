
file = open('numbers.txt', 'r', encoding='utf-8')

numbers = list(map(int, (map(str.strip, file.readlines()))))

print(sum(numbers))

file.close()

# file = open('numbers.txt')
#
# print(sum(map(int, file)))
#
# file.close()