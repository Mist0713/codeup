import sys
input = sys.stdin.readline

money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
cnt = 0
N = int(input())
for coin in money:
    cnt += N // coin
    N %= coin
print(cnt)