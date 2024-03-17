import sys


input = sys.stdin.readline
N = int(input().strip())
min_value = N
init_sum = sum(map(int, list(str(N))))
for c in range(max(N - 54, 1), max(N - init_sum + 1, N)):
    if N == c + sum(map(int, list(str(c)))) and min_value > c:
        min_value = c

if min_value == N:
    print(0)
else:
    print(min_value)
