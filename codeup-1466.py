import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [[1 for _ in range(m)] for _ in range(n)]
cnt = 0

for i in range(m-1, -1, -1):
    for j in range(n-1, -1, -1):
        lst[j][i] += cnt
        cnt += 1

print(*[' '.join(map(str, row)) for row in lst], sep='\n')