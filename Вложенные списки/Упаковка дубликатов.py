st = input().split()

# This will be the list to hold our packed sublists
packed_list = []
# Temporary sublist for current sequence of identical elements
sub = []

# Iterate over each element in the input list
for i in st:
    # If the temporary sublist is empty or current element matches the last in the sublist, append it
    if not sub or sub[-1] == i:
        sub.append(i)
    else:
        # If current element is different, add the sublist to packed_list and start a new sublist
        packed_list.append(sub)
        sub = [i]

# Don't forget to add the last sublist to packed_list if sub is not empty
if sub:
    packed_list.append(sub)

print(packed_list)

# res = []
#
# for el in input().split():
#     if res and el in res[-1]:
#         res[-1].append(el)
#     else:
#         res.append([el])
#
# print(res)