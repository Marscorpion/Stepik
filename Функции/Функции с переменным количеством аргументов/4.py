def greet(name, *args):
    return f"Hello, {name} and {' and '.join(args)}!" if args else f'Hello, {name}!'

# def greet(name, *args):
#     return f'Hello, {" and ".join((name,) + args)}!'

print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))
