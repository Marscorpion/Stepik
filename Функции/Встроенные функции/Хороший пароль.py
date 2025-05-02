password = input()
#
result = all([any(c.isdigit() for c in password), any(c.islower() for c in password), any(c.isupper() for c in password), len(password) >= 7])

print(('NO', 'YES')[result])





