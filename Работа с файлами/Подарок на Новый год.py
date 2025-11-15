with open('class_scores.txt', 'r') as scores, open('new_scores.txt', 'w') as new_scores:
    for line in scores:
        n, p = line.split(' ')
        print(*[f'{n} {int(p) + 5 if int(p) < 96 else 100}'], file=new_scores)


# with open('class_scores.txt') as class_scores, open('new_scores.txt', 'w') as new_scores:
#     for line in class_scores:
#         name, score = line.split()
#         score = int(score) + 5
#         if score > 100:
#             score = 100
#         print(name, score, file=new_scores)