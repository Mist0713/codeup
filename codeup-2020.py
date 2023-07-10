import sys
input = sys.stdin.readline

symbol = ['I','V','X','L','C','D','M']
baseValue = [1, 5, 10, 50, 100, 500, 1000]

string = input().rstrip()
result = baseValue[symbol.index(string[len(string)-1])] * int(string[len(string)-2])

for i in range(3, len(string), 2):
    if symbol.index(string[i]) <= symbol.index(string[i-2]):
        result += baseValue[symbol.index(string[i-2])] * int(string[i-3])
        # print(i, result)
    else:
        result -= baseValue[symbol.index(string[i-2])] * int(string[i-3])
        # print(i, result)

print(result)