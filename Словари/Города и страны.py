countries = {
    "Sweden": ["Stockholm", "Göteborg", "Malmö"],
    "Norway": ["Oslo", "Bergen", "Trondheim"],
    "England": ["London", "Birmingham", "Manchester"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "France": ["Paris", "Marseille", "Toulouse"]
}

city = input()

# for key, value in countries.items():
#     if city in value:
#         print(f'INFO: {city} is a city in {key}')
#         break
# else:
#     print(f'ERROR: Country for {city} not found')

for i in countries:
    if city in countries[i]:
        print(f'INFO: {city} is a city in {i}')
        break
else:
    print(f'ERROR: Country for {city} not found')

# country = [k for k, v in countries.items() if city in v]
# print(f'INFO: {city} is a city in {country[0]}' if country else f'ERROR: Country for {city} not found')
# print(country)