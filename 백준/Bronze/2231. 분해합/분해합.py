import sys


input = sys.stdin.readline
N = int(input().strip())
min_value = N
for c in range(N, 1, -1):
    if N == c + sum(map(int, list(str(c)))) and min_value > c:
        min_value = c

if min_value == N:
    print(0)
else:
    print(min_value)