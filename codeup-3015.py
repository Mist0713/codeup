n, m = map(int, input().split())
lst = []
for i in range(n):
    a, b = input().split()
    b = int(b)
    lst.append((a, b))

lst2 = sorted(lst, key=lambda x: x[1]*(-1))
for i in range(m):
    print(lst2[i][0])