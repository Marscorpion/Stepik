ip = input().split('.')
#
print(all(c.isdigit() and 0 <= int(c) <= 255 for c in ip))

# print(all(lambda c: c.isdigit() and 0 <= int(c) <= 255 for c in ip))

