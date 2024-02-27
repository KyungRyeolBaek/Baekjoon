import sys


def MenOfPassion(n, count=0, bigO=0):
    sum = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            sum += i * j
            count += 1
    bigO += 2
    return sum, count, bigO


input = sys.stdin.readline
print(int(input().strip())**2)
print(2)