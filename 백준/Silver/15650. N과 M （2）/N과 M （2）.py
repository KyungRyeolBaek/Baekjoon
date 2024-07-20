import sys
from itertools import combinations


input = sys.stdin.readline
N, M = map(int, input().strip().split())
for result in combinations([n for n in range(1, N + 1)], M):
    print(' '.join(map(str, result)))