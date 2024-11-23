
print(len(max(input().split('О'))))

list_letter = input().split('О')
count = 0
for i in list_letter:
    if len(i) > count:
        count = len(i)

print(count)

s = input()
seq = s.split("О")  # убираем всех орлов и группируем решек

mx = 0  # максимум подряд идущих решек
for el in seq:
    mx = max(mx, el.count("Р"))

print(mx)