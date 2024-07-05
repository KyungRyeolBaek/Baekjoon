import sys


def fibonacci(n):
    if n == 0:
        return 0
    if n == (1 or 2):
        return 1
    DP = [1, 1]
    for i in range(1, n - 1):
        DP.append(DP[i] + DP[i - 1])
    return DP[n - 1]


input = sys.stdin.readline
n = int(input().strip())
print(fibonacci(n))