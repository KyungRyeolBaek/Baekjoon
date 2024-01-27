import sys


input = sys.stdin.readline

N = int(input().strip())
square = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(N):
    x1, y1 = map(int, input().strip().split())
    for x in range(x1 - 1, x1 + 9):
        for y in range(y1 - 1, y1 + 9):
            square[y][x] = 1
result = 0
for s in square:
    result += sum(s)
print(result)
