import sys
input = sys.stdin.readline

n = int(input())
tunnel = list(map(int, input().split()))
result = sys.maxsize
for i in range(5):
    if abs(n-tunnel[i]) < result:
        result = abs(n-tunnel[i])
print(result)