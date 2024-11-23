n = int(input())

class_list = [tuple(input().split()) for _ in range(n)]

for rows in class_list:
    print(*rows)

print()

for rows in class_list:
    if int(rows[1]) > 3:
        print(*rows)

# for name, grade in class_list:
#     if int(grade) > 3:
#         print(name, grade)
