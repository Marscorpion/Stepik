files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']

set_files = {file.lower() for file in files if file.lower()[-3 ::] == 'png'}

# result = {c.lower() for c in files if c.lower().endswith('.png')}

print(*sorted(set_files))