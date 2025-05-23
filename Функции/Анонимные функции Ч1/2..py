from functools import reduce

data = [['Tokyo', 35676000, 'primary'],
        ['New York', 19354922, 'nan'],
        ['Mexico City', 19028000, 'primary'],
        ['Mumbai', 18978000, 'admin'],
        ['Sao Paulo', 18845000, 'admin'],
        ['Delhi', 15926000, 'admin'],
        ['Shanghai', 14987000, 'admin'],
        ['Kolkata', 14787000, 'admin'],
        ['Los Angeles', 12815475, 'nan'],
        ['Dhaka', 12797394, 'primary'],
        ['Buenos Aires', 12795000, 'primary'],
        ['Karachi', 12130000, 'admin'],
        ['Cairo', 11893000, 'primary'],
        ['Rio de Janeiro', 11748000, 'admin'],
        ['Osaka', 11294000, 'admin'],
        ['Beijing', 11106000, 'primary'],
        ['Manila', 11100000, 'primary'],
        ['Moscow', 10452000, 'primary'],
        ['Istanbul', 10061000, 'admin'],
        ['Paris', 9904000, 'primary']]

filter_city = filter(lambda city: city[1] > 10000000 and city[2] == 'primary', data)
sorted_names = sorted(map(lambda c: c[0], filter_city))
result = reduce(lambda x, y: x + ", " + y, sorted_names)
# result = reduce(lambda city1, city2: f'{city1}, {city2}', sorted_names)
# result = ', '.join(sorted_names)
# print(reduce(lambda s1,s2: s1+", "+s2 if s1!="Cities: " else s1+s2, sorted_names, "Cities: "))

print(f'Cities: {result}')