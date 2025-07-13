import sys
input = sys.stdin.readline

N = int(input())
lst = [[0 for _ in range(N)] for _ in range(N)]

x, y = 0, N//2

lst[x][y] = 1
for i in range(2, N*N + 1):
    if i