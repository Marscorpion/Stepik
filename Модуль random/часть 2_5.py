from random import shuffle

word = list(input())
shuffle(word)
print(*word, sep='')
