import sys
input = sys.stdin.readline

for i in range(1, 10):
    for j in range(2, 6):
        print(j, "x", i, "=", sep=" ", end="")
        print(" %2d" % (i*j), end="")
        if j!=5:
            print("\t", end="")
    print()