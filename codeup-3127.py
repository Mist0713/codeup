a = input().split()
stack = []

for i in a:
    stack.append(i)
    if stack[-1] == '*':
        b = int(stack[-3]) * int(stack[-2])
        for _ in range(3):
            stack.pop()
        stack.append(b)
    elif stack[-1] == '+':
        c = int(stack[-3]) + int(stack[-2])
        for _ in range(3):
            stack.pop()
        stack.append(c)
    elif stack[-1] == '-':
        d = int(stack[-3]) - int(stack[-2])
        for _ in range(3):
            stack.pop()
        stack.append(d) 

print(stack[0])
    