def matrix(n=1, m=None, value=0):
    if m is None:
        m=n
    res = [[value] * m for _ in range(n)]
    return res

print(matrix(3))