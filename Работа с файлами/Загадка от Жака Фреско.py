
with open('goats.txt', 'r') as goats, open('answer.txt', 'w') as answers:
    text = [lines.strip() for lines in goats.readlines()]
    text1, text2 = text[1:text.index('GOATS')], text[text.index('GOATS')+1:]
    # print(*sorted(filter(lambda x: text2.count(x) / len(text2) > 0.07, text1)), sep='\n', file=answers)

    res = {}
    for a in text2:
        res[a] = res.get(a, 0) + 1

    result = []
    for key, value in res.items():
        if int(value / sum(res.values()) * 100) > 7:
            result.append(key)

    # print(*sorted(result), sep='\n', file=answers)

    # [answers.write(k) for k in res if res[k] >= len(text2) * .07]
    print(*[k for k in res if res[k] >= len(text2) * .07], sep='\n', file=answers)


