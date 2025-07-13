import sys
input = sys.stdin.readline

vowelASCII = [97, 101, 105, 111, 117] # a, e, i, o, u

def rovarsparket(asciiDec):
    print(chr(asciiDec), end='')
    if asciiDec in vowelASCII:
        return
    else:
        if asciiDec>117:
            print(chr(117), end='')
        else:
            a = b = asciiDec
            while a not in vowelASCII and b not in vowelASCII:
                a -= 1
                b += 1
            print(chr(a if a in vowelASCII else b), end='')
        if asciiDec == 122: # z
            print('z', end='')
        else:
            print(chr(asciiDec+2 if asciiDec+1 in vowelASCII else asciiDec+1), end='')

lst = [ord(char) for char in input().strip()]

for char in lst:
    rovarsparket(char)