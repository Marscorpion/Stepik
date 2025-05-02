
abscissas = list(map(float, input().split()))
ordinates = list(map(float, input().split()))
applicates = list(map(float, input().split()))



# points = list(zip(abscissas, ordinates, applicates))
#
# print(all(map(lambda x: x[0] ** 2 + x[1] ** 2 + x[2] ** 2 <= 4, *points)))

print(all(x ** 2 + y ** 2 + z ** 2 <= 4 for x, y, z in zip(abscissas, ordinates, applicates)))

# print(all(x**2 + y**2 + z**2 <= 4 for x, y, z in zip(abscissas, ordinates, applicates)))

# print(all(map(lambda x, y, z: x**2 + y**2 + z**2 <= 4, abscissas, ordinates, applicates)))





