import sys
input = sys.stdin.readline

string = input().rstrip()
length = len(string)
string += '*'

for i in range(length):
    if string[i].isalpha():
        if string[i+1]

