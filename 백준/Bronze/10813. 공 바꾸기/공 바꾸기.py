import sys


input = sys.stdin.readline
N, M = map(int, input().strip().split())
box = [str(i + 1) for i in range(N)]
for _ in range(M):
    i, j = map(int, input().strip().split())
    box[i-1], box[j-1] = box[j-1], box[i-1]
print(' '.join(box))