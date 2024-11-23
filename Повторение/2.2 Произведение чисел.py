num = int(input())

n = [int(input()) for _ in range(num)]

x = int(input())

found = False
for i in range(len(n)):
    for j in range(i + 1, len(n)):
        if n[i] * n[j] == x:
            found = True
            break
    if found:
        break

if found:
    print('ДА')
else:
    print('НЕТ')


numbers, multiply = [int(input()) for i in range(int(input()))], int(input())
for i in range(len(numbers)-1):
    for j in range(i+1, len(numbers)):
        if multiply == numbers[i] * numbers[j]:
            exit(print("ДА"))
print("НЕТ")










