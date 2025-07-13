import sys
input = sys.stdin.readline

for i in range(int(input())):
    for j in range(i):
        print(' ', end='')
    print('**')
