import random, string

# def generate_password(length):
#     symbols = [item for item in (string.ascii_letters + string.digits) if item not in 'lI1oO0']
#     password = []
#     for i in range(length):
#         password.append(symbols[random.randrange(0, len(symbols))])
#     return ''.join(password)
#
#
# def generate_passwords(count, length):
#     passwords = []
#     for i in range(count):
#         passwords.append((generate_password(length)))
#     return passwords

symbols = [item for item in (string.ascii_letters + string.digits) if item not in 'lI1oO0']

def generate_password(length):
    return ''.join([symbols[random.randrange(0, len(symbols))] for _ in range(length)])
    # return ''.join(sample(symbols, length))
def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]

    # def generate_passwords(count, length):
    #     for i in range(count):
    #         print(generate_password(length))

n, m = int(input()), int(input())

print(*generate_passwords(n, m), sep='\n')
# generate_passwords(int(input()), int(input()))


