n = int(input())

infected_ref = []

a = 'anton'

for c in range(n):
    code = input()
    pointer = 0

    for char in code:
         if char == a[pointer]:
            pointer += 1  # Move to the next character in 'anton'
            if pointer == len(a):  # If all characters in 'anton' matched
                infected_ref.append(c + 1)
                break  # Exit the loop

print(*infected_ref)

# n = int(input())
# for i in range(n):
#     seq = ["a", "n", "t", "o", "n"]
#     s = list(input())
#
#     while seq and s:  # пока у нас непустые список из букв строки и список слова "anton"
#         if seq[0] == s[0]:  # если буквы равны, то вырываем и там, и там
#             seq.pop(0)
#             s.pop(0)
#         else:  # иначе вырываем только из списка букв строки
#             s.pop(0)
#
#     # если список букв слова "anton" пустой, значит вырвали все буквы,
#     # значит в строке встретились все эти буквы в нужном нам порядке
#     if not seq:
#         print(i + 1, end=" ")