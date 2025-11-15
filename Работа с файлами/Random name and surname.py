import random

with open("first_names.txt") as name_file, open("last_names.txt") as lname_file:

    n = name_file.read().split()
    ln = lname_file.read().split()

    names = []
    for _ in range(3):
        names.append((*random.sample(n, k=1), *random.sample(ln, k=1)))
    for n, ln in names:
        print(n, ln)

    # names = []
    # lnames = []
    # for _ in range(3):
    #     names.append(*random.sample(n, k=1))
    #     lnames.append(*random.sample(ln, k=1))
    #     name_file.seek(0)
    #     lname_file.seek(0)

    # names_dict = dict(zip(names, lnames))
    # for k, v in names_dict.items():
    #     print(k, v)

# with open('first_names.txt', 'r', encoding='utf-8') as f, open('last_names.txt', 'r', encoding='utf-8') as l:
#     z, x = f.readlines(), l.readlines()
#     for i in range(3):
#         print(random.choice(z).strip(), random.choice(x).strip(), sep=' ')









