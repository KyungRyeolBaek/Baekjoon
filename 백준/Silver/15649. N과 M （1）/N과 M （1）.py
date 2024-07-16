import sys
from itertools import permutations


input = sys.stdin.readline
N, M = map(int, input().strip().split())
results = list(permutations([str(n) for n in range(1, N + 1)], M))
for result in results:
    print(' '.join(result))