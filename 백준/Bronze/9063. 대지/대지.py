import sys


input = sys.stdin.readline
N = int(input().strip())
x = []
y = []
for _ in range(N):
    a, b = map(int, input().strip().split())
    x.append(a)
    y.append(b)
print((max(x) - min(x)) * (max(y) - min(y)))