import sys
input = sys.stdin.readline
operators = ['+', '-', '*', '/', '=']

lst = list(input().rstrip())
quary = []
buf = ''

for i in range(len(lst)):
    if lst[i] in operators:
        quary.append(buf)
        buf = ''
        quary.append(lst[i])
    else:
        buf += lst[i]

result = int(quary.pop(0))

while quary:
    cnt = quary.pop(0)
    if cnt =='=':
        print(result)
        break
    elif cnt == '+':
        result += int(quary.pop(0))
    elif cnt == '-':
        result -= int(quary.pop(0))
    elif cnt == '*':
        result *= int(quary.pop(0))
    elif cnt == '/':
        result //= int(quary.pop(0))

