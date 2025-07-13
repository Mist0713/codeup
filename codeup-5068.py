import sys
input = sys.stdin.readline

m = int(input())
d = int(input())

if m==2:
    if d==18:
        print("Special")
    else:
        print("After" if d>18 else "Before")
else:
    print("After" if m>2 else "Before")