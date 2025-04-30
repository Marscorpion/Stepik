numbers = input().split()

def summ(num):
    num = [int(i) for i in num]
    return sum(num)

print(*sorted(numbers, key=summ))



