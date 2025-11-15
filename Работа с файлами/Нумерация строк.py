# with open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w') as output_file:
#     text = [lines.strip() for lines in input_file.readlines()]
#     # for c in range(len(text)):
#     #     print(f'{c+1}) {text[c]}')
#     print(*[f'{c+1}) {text[c]}' for c in range(len(text))], sep='\n', file=output_file)

with open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w') as output_file:
    print(*[f'{i}) {line}' for i, line in enumerate (input_file, 1)], file=output_file)


# with open('output.txt', 'r') as output_file:
#     new_text = output_file.read()
#     print(new_text)