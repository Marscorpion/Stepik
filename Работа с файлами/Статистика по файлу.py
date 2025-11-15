with open('file.txt') as f:
    text = f.read()
    stroka = ''.join(c if c.isalpha() else '' for c in text)

    f.seek(0)
    print(f'Input file contains:')
    print(f'{len(stroka)} letters')
    print(f'{len(f.read().split())} words')
    f.seek(0)
    print(f'{len(f.readlines())} lines')

# with open('lines.txt') as f:
#     txt = f.read()
#     print('Input file contains:')
#     print(sum(map(str.isalpha, txt)), 'letters')
#     print(len(txt.split()), 'words')
#     print(txt.count('\n') + 1, 'lines')