import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(abs(a[i]-b[i]) for i in range(N))
result = 0
select_a, select_b = 0, 0

for i in range(N):
    if a[i]>b[i]:
        result += a[i]
        select_a += 1
    else:
        result += b[i]
        select_b += 1

if (0 in c) or select_a*select_b != 0:
    print(result)
else:
    print(result - min(c))
