import sys


input = sys.stdin.readline
N, M = map(int, input().strip().split())
box = ['0' for _ in range(N)]
for _ in range(M):
    i, j, k = map(int, input().strip().split())
    for n in range(i - 1, j):
        box[n] = str(k)
print(' '.join(box))
