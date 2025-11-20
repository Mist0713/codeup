import sys
input = sys.stdin.readline

K, N = map(int, input().split())
cnt = 0
while K>=N:
    cnt +=1
    K -= N-1
print(cnt)