import sys


input = sys.stdin.readline
N, M = map(int, input().strip().split())
box = [str(i) for i in range(N + 1)]
for _ in range(M):
    i, j = map(int, input().strip().split())
    box[i:j + 1] = box[j:i - 1:-1]
print(' '.join(box[1:]))