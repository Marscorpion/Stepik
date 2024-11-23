dial={".":'1', ",":'11', "?":'111', "!":'1111', ":":'11111',
    "A":'2', "B":'22', "C":'222',
    "D":'3', "E":'33', "F":'333',
    "G":'4', "H":'44', "I":'444',
    "J":'5', "K":'55', "L":'555',
    "M":'6', "N":'66', "O":'666',
    "P":'7', "Q":'77', "R":'777', "S": '7777',
    "T":'8', "U":'88', "V":'888',
    "W":'9', "X":'99', "Y":'999', "Z": '9999',
    " ":'0'
}

n = input().upper()

print(*[dial[i] for i in n if i in dial], sep='')

# keyboard = {
#     "1": ".,?!:",
#     "2": "ABC",
#     "3": "DEF",
#     "4": "GHI",
#     "5": "JKL",
#     "6": "MNO",
#     "7": "PQRS",
#     "8": "TUV",
#     "9": "WXYZ",
#     "0": " "
# }
#
# for letter in input().upper():
#     for key, value in keyboard.items():
#         if letter in value:
#             print(key * (value.index(letter) + 1), end="")

# num = {'.,?!:': '1', 'ABC': '2', 'DEF': '3',
#        'GHI': '4', 'JKL': '5', 'MNO': '6',
#        'PQRS': '7', 'TUV': '8', 'WXYZ': '9',
#        ' ': '0'}
# for l in input().upper():
#     [print(num[i] * (i.index(l) + 1), end='') for i in num if l in i]