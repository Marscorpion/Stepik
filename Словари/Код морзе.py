letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']

morse_abs = dict(zip(letters, morse))

# morse_abs = {letters[i]:morse[i] for i in range(len(letters))}

n = input().upper()


print(*[morse_abs[i] for i in n if i in morse_abs])

# for c in n:
#     if c in morse_abs:
#         print(morse_abs[c], end=' ')