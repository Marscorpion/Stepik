n = int(input())

with open('output_.txt', 'w') as out:
    for _ in range(n):
        fname = input().strip()
        with open(fname, 'r') as f:
            out.write(f.read())

# for i in range(int(input())):
#     with open(input()) as inp, open('output.txt', 'a') as out:
#         print(inp.read(), file=out, end='')
