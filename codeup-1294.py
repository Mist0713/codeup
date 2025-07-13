import sys
input = sys.stdin.readline

string = input().rstrip()

alpahbet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

encode = ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c']

encoded_string = ''
for char in string:
    if char in alpahbet:
        index = alpahbet.index(char)
        encoded_string += encode[index]
    else:
        encoded_string += char
print(encoded_string)