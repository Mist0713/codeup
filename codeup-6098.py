import sys
input = sys.stdin.readline

def pr(lst):
    for i in lst:
        print(*i)

lst = [list(map(int, input().split())) for _ in range(10)]
lst[1][1] = 9  # Starting point
x, y = 1, 1
while True:
    if (x>= 9 and y >= 9) or (lst[x][y+1] == 1 and lst[x+1][y] == 1):
        pr(lst)
        break
    if lst[x][y+1] != 1:
        if lst[x][y+1] == 2:
            lst[x][y+1] = 9
            pr(lst)
            break
        else:
            lst[x][y+1] = 9
            y += 1
    elif lst[x+1][y] != 1:
        if lst[x+1][y] == 2:
            lst[x+1][y] = 9
            pr(lst)
            break
        else:
            lst[x+1][y] = 9
            x += 1