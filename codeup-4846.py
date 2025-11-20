import sys
input = sys.stdin.readline

school, apple = [], []

cnt = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    cnt += b % a

print(cnt)
