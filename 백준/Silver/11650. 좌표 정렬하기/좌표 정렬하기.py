import sys


input = sys.stdin.readline
N = int(input())
values = []
for _ in range(N):
    values.append(list(map(int, input().strip().split())))

values.sort(key=lambda x: (x[0], x[1]))

for value in values:
    print(' '.join(map(str, value)))