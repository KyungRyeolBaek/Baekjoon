import sys


input = sys.stdin.readline
point = []
for i in range(3):
    x, y = map(int, input().strip().split())
    point.append((x, y))
result = []
for i in range(2):
    if point[0][i] == point[1][i]:
        result.append(str(point[2][i]))
    elif point[0][i] == point[2][i]:
        result.append(str(point[1][i]))
    else:
        result.append(str(point[0][i]))

print(' '.join(result))