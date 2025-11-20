import sys
input = sys.stdin.readline

N = int(input())
lst = [[1 for _ in range(N)] for _ in range(N)]
cnt = 0

for i in range(N):
    if i % 2 == 0:
        for j in range(N):
            lst[j][i] += cnt
            cnt += 1
    else:
        for j in range(N-1, -1, -1):
            lst[j][i] += cnt
            cnt += 1

print(*[' '.join(map(str, row)) for row in lst], sep='\n')