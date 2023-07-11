import sys
input = sys.stdin.readline
result = 0
a, b = map(int, input().split())
flag = 0
for i in range(1, a+1):
    if a%i == 0:
        flag += 1
    if flag == b:
        result = i
        break
print(result)