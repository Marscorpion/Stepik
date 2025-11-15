with open('nums.txt') as file:
    text = file.read()
    nums = ''.join(c if c.isdigit() else ' ' for c in text)
    # numbers = [int(num) for num in nums.split()]
    # print(sum(numbers))
    print(sum(map(int, nums.split())))

# print(sum(map(int, ''.join((' ', c)[c.isdigit()] for c in open('numbers.txt').read()).split())))



