symbols = input()
code = {}

for c in symbols:
    code[c] = code.get(c, 0) + 1

cipher = ''.join(str(code[c]) for c in symbols)

letters = {}

n = int(input())
for c in range(n):
    letter, count=input().split(': ')
    letters[count] = letter

word = ''.join(str(letters[c]) for c in cipher)

print(word)








