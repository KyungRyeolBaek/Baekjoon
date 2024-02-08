import sys


input = sys.stdin.readline
N, K = map(int, input().strip().split())
n = 1
while K:
    if N % n == 0:
        K -= 1
    n += 1
    if n > N:
        break
if K:
    print(0)
else:
    print(n - 1)
