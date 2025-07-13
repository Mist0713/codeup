import sys
input = sys.stdin.readline

a, b = map(int, input().split())
memo = [0] * 10000001 #500000까지의 범위 중 3n+1로 도달가능한 최대의 수+1
memo[1] = 1

max_length, index = 0, 1

def lengthOfCollatz(n):
    count = 1
    while n != 1:
        if n < 10000001 and memo[n] != 0:
            return count + memo[n]-1
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        count += 1
    return count

for i in range(a, b+1):
    current_length = lengthOfCollatz(i)
    memo[i] = current_length
    if current_length > max_length:
        max_length = current_length
        index = i

print(f"{index} {max_length}")