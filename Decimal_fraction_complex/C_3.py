n, a, b = int(input()), input(), input()
z1 = complex(a)
z2 = complex(b)

print(z1 ** n + z2 ** n + z1.conjugate() ** n + z2.conjugate() ** (n+1))