import sys
input = sys.stdin.readline

N = int(input())

def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("prime" if isPrime(N) else "composite")