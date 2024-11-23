import random, string

def generate_password(length):
    symbols = [item for item in (string.ascii_letters + string.digits) if item not in 'lI1oO0']
    password = []
    for i in range(length):
        password.append(symbols[random.randrange(0, len(symbols))])
    return ''.join(password)

def generate_passwords(count, length):
    passwords = []
    for i in range(count):
        passwords.append((generate_password(length)))
    return passwords

n, m = int(input()), int(input())

print(*generate_passwords(n, m), sep='\n')