countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]



for i in zip(countries, capitals, population):
    print(f'{i[1]} is the capital of {i[0]}, population equal {i[2]} people.')

# print(*[f'{i[1]} is the capital of {i[0]}, population equal {i[2]} people.' for i in zip(countries, capitals, population)], sep='\n')

# for country, capital, people in zip(countries, capitals, population):
#     print(f'{capital} is the capital of {country}, population equal {people} people.')
