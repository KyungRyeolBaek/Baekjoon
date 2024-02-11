import sys


input = sys.stdin.readline
N = int(input().strip())

while N != 1:
    for n in range(2, N + 1):
        q, r = divmod(N, n)
        if r == 0:
            N = q
            print(n)
            break