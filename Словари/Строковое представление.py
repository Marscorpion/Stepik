n = input()

numbers = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}

# for i in n:
#     print(numbers[i], end=' ')

print(*[numbers[i] for i in n if i in numbers])

# print(*[numbers[key] for key in input()])