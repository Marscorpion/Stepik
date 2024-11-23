
words = [input().lower() for _ in range(int(input()))]

unique_letters = set(words[0]).union(*words)

print(len(unique_letters))

n = int(input())

word = set(input().lower())

for _ in range(n-1):
    word.update(set(input().lower()))

print(len(word))

n = int(input())
symbols = set()

for _ in range(n):
    for c in input().lower():
        symbols.add(c)

print(len(symbols))