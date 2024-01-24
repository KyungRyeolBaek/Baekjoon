import sys


input = sys.stdin.readline
N, M = map(int, input().strip().split())
A = [list(map(int, input().strip().split())) for _ in range(N)]
B = [list(map(int, input().strip().split())) for _ in range(N)]
for i, bi in enumerate(B):
    for j, bj in enumerate(bi):
        A[i][j] = str(A[i][j] + bj)

for a in A:
    print(' '.join(a))
