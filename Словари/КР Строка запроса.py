def build_query_string(params):
    sorted_params = sorted(params.items())
    query_string_parts = [f'{key}={value}' for key, value in sorted_params]
    return '&'.join(query_string_parts)



print(build_query_string({'name': 'timur', 'age': 28}))
print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))

