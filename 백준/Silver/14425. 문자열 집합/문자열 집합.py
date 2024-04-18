import sys


input = sys.stdin.readline
N, M = map(int, input().strip().split())
S = set(input().strip() for _ in range(N))
count = 0
for _ in range(M):
    if input().strip() in S:
        count += 1
print(count)