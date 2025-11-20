import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [i+1 + m*(n-1) for i in range(m)]
for i in range(n):
    print(' '.join(map(str, lst)))
    for j in range(m):
        lst[j] -= m
