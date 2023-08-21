import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

for i in range(n):
    print(*lst, sep=" ")
    lst.append(lst.pop(0))
