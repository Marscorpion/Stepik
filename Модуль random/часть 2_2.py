from random import  randrange as r

def generate_index():
    return f'{chr(r(65, 91))}{chr(r(65, 91))}{r(0, 100)}_{r(0, 100)}{chr(r(65, 91))}{chr(r(65, 91))}'

print(generate_index())

# import string
# from random import choice, randrange as r
#
# letter = string.ascii_uppercase
#
# def generate_index():
#     return f'{choice(letter)}{choice(letter)}{r(0, 100)}_{r(0, 100)}{choice(letter)}{choice(letter)}'
#
# print(generate_index())
