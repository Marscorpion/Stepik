import random, string

symbols = [item for item in (string.ascii_letters + string.digits) if item not in 'lI1oO0']
s = [item for item in (string.ascii_uppercase) if item not in 'lI1oO0']
s1 = [item for item in (string.ascii_lowercase) if item not in 'lI1oO0']
s2 = [item for item in (string.digits) if item not in 'lI1oO0']


def generate_password(length):
    # password = []
    #
    # password.append(random.choice(s))
    # password.append(random.choice(s1))
    # password.append(random.choice(s2))
    # for i in range(length-3):
    #         password.append(symbols[random.randrange(0, len(symbols))])

    password = [random.choice(i) for i in (s, s1, s2,)] + [random.choice(symbols) for _ in range(length - 3)]
    random.shuffle(password)
    return ''.join(password)

def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]



n, m = int(input()), int(input())

print(*generate_passwords(n, m), sep='\n')