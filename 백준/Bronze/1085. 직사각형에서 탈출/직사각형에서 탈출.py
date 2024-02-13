import sys


input = sys.stdin.readline
x, y, w, h = map(int, input().strip().split())
result = [x, y]
result.append(w - x)
result.append(h - y)
print(min(result))