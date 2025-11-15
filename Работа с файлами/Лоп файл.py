with open('logfile.txt', 'r') as log, open('output3.txt', 'w') as out:
    date = [line.strip().split(',') for line in log.readlines()]
    for line in date:
        a = int(line[1][:3]) * 60 + int(line[1][4 :])
        b = int(line[2][:3]) * 60 + int(line[2][4 :])
        if b-a >= 60:
            print(line[0], file=out)

# with open('logfile.txt', encoding='utf-8') as fr, open('output3.txt', 'a', encoding='utf-8') as fw:
#     for line in fr:
#         name, st, en = line.split(', ')
#         if int(en.replace(':', '')) - int(st.replace(':', '')) >= 100:
#             print(name, file=fw)

# def get_minutes(x):
#     h, m = map(int, x.split(':'))
#     return h * 60 + m

# with open('logfile.txt', encoding='utf-8') as file, open('output3.txt', 'w', encoding='utf-8') as out:
#     for line in file:
#         name, a, b = line.rstrip().split(',')
#         if (get_minutes(b) - get_minutes(a)) >= 60:
#             print(name, file=out)