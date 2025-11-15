def read_csv():
    with open('data.csv') as file:
          text = [line.strip().split(',') for line in file.readlines()]
          text1 = []
          for line in text[1 ::]:
              text1.append(dict(zip(text[0], line)))
          return (text1)


print(read_csv())

# def read_csv():
#     with open('data.csv', encoding='utf-8') as file:
#         lines = [line.strip().split(',') for line in file]
#         keys = lines[0]
#         return [dict(zip(keys, values)) for values in lines[1:]]
#
# print(read_csv())


# def read_csv():
#     with open('data.csv') as file:
#         keys = file.readline().strip().split(',')
#         return [dict(zip(keys, line.strip().split(','))) for line in file]