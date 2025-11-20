h, k, d = input().split()
h, k = int(h), int(k)

char = '*' * k
if d =='L':
    for i in range(h):
        print(' '*i, end='')
        print(char)
elif d == 'R':
    for i in range(h):
        print(' ' * (h - i -1), end='')
        print(char)
