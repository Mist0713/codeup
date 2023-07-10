import sys
input = sys.stdin.readline

graph = []
answer = [[] for _ in range(25)]

for _ in range(25):
    graph.append(list(map(int, input().split())))

print('--------------------------------------------------')

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]

def isSurvive(a, b):
    temp = 0
    for i in range(8):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0<=nx<25 and 0<=ny<25:
            if graph[nx][ny] == 1:
                temp += 1
    if graph[a][b] == 1:
        if temp>=4 or temp<=1:
            return 0
        else:
            return 1
    else:
        if temp == 3:
            return 1
        else:
            return 0

for i in range(25):
    for j in range(25):
        answer[i].append(isSurvive(i, j))

for i in range(25):
    print(*answer[i], sep=' ')
