import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    lst = ["*"] + [" "] * (n//2 -1) + ["*"] + [" "] * (n//2 -1) + ["*"]
    if i ==0 or i == n - 1 or i == n // 2:
        print("*" * n)
    else:
        lst[i] = "*"
        lst[n - i - 1] = "*"
        print("".join(lst))

