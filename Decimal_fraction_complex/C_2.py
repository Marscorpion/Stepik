numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]

d = {i : abs(i) for i in numbers}
m = max(d.values())
print(*[k for k in d if d[k] == m], m, sep='\n')

# print(max(numbers, key=abs), sep='\n')
#
# print(max(abs(i) for i in numbers))

# m = max(abs(i) for i in numbers)
#
# for i in numbers:
#     if abs(i) == m:
#         print(i, m, sep='\n')