import sys


input = sys.stdin.readline
max_value = 0
idx = [0, 0]
for i in range(9):
    for j, value in enumerate(map(int, input().strip().split())):
        if value >= max_value:
            max_value = value
            idx = [str(i + 1), str(j + 1)]
print(max_value)
print(' '.join(idx))