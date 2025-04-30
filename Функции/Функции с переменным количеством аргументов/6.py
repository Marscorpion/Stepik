def info_kwargs(**kwargs):
    for key, value in sorted(kwargs.items()):
       print(f'{key}: {value}')

# def info_kwargs(**kwargs):
#     [print(f'{key}: {kwargs[key]}') for key in sorted(kwargs.keys())]

# def info_kwargs(**kwargs):
#     print('\n'.join(f'{k}: {v}' for k, v in sorted(kwargs.items())))


info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')