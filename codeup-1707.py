import sys
input = sys.stdin.readline

def roundTraditional(val, digits):
    return round(val+10**(-len(str(val))-1), digits)

lst = list(map(int, input().split()))

avg = sum(lst)/10

upper = []
for i in range(10):
    if lst[i]>=avg:
        upper.append(lst[i])

print(roundTraditional(avg, 1))
print(len(upper), 10-len(upper))

