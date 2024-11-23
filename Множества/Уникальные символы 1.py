n = int(input())

unique_char = []

for i in range(n):
    word = input().lower()
    print(len(set(word)))

# for _ in range(int(input())):
#     print(len(set(input().lower())))