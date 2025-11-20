import sys
input = sys.stdin.readline

N = int(input())

cnt = 1
for i in range(N):
    if i % 2 != 0:
        for j in range(N):
            print(cnt, end=' ')
            cnt += 1
    else:
        temp = cnt + N - 1
        for j in range(N):
            print(temp, end=' ')
            temp -= 1
        cnt += N
    print()