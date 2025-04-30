is_num = lambda c: '-' not in c[1::] and c.replace('.', '0', 1).replace('-', '', 1).isdigit()

# is_non_negative_num = lambda q: q.replace('.', '', 1).isdigit()
#
# is_num = lambda q: is_non_negative_num(q[1:]) if q[0] == '-' else is_non_negative_num(q)

print(is_num('10.34ab'))
print(is_num('10.45'))
print(is_num('-18'))
print(is_num('-34.67'))
print(is_num('987'))
print(is_num('abcd'))
print(is_num('123.122.12'))
print(is_num('-123.122'))
print(is_num('--13.2'))