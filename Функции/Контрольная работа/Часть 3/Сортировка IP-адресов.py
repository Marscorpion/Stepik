from functools import reduce

n = int(input().strip())
ips = [input().strip() for _ in range(n)]


key = lambda ip: reduce(
    lambda acc, octet: acc * 256 + octet,
    map(int, ip.split('.')),
    0
)

ips.sort(key=key)

print('\n'.join(ips))

