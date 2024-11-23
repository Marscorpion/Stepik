from random import  randint

def generate_ip():
    ip_parts = [str(randint(0, 255)) for _ in range(4)]

    return '.'.join(ip_parts)

    # return '.'.join([str(randint(0, 255)) for _ in range(4)])

print(generate_ip())



# for _ in range(4):
#     print(randint(0, 255), end='.')

# print(*(randint(0, 255) for _ in range(4)),  sep='.')

# from random import randrange as r
#
# def generate_ip():
#     return f'{r(256)}.{r(256)}.{r(256)}.{r(256)}'