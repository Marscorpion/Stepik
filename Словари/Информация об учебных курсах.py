courses = {'CS101': ['3004', 'Хайнс', '8:00'],
           'CS102': ['4501', 'Альварадо', '9:00'],
           'CS103': ['6755', 'Рич', '10:00'],
           'NT110': ['1244', 'Берк', '11:00'],
           'CM241': ['1411', 'Ли', '13:00']}

n = input()


print(f'{n}: {courses[n][0]}, {courses[n][1]}, {courses[n][2]}')

# print('{}: {}, {}, {}'.format(n, *courses[n]))

# aud, teacher, time = courses[n]
# print(f'{n}: {aud}, {teacher}, {time}')

