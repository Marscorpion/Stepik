emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
          'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
          'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
          'yandex.ru': ['surface', 'google'],
          'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
          'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}

# email = []
# for k, v in emails.items():
#     for i in v:
#         email.append(f'{i}@{k}')
# print(*sorted(email), sep='\n')

# print(*sorted([i+'@'+k for k, v in emails.items() for i in v]), sep = '\n')

print(*sorted([f'{i}@{k}' for k, v in emails.items() for i in v]), sep='\n')