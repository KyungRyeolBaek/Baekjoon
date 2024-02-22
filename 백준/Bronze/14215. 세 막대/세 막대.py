import sys


input = sys.stdin.readline
tri = list(map(int, input().strip().split()))
tri.sort()
a, b, c = tri
if a + b > c:
    print(sum(tri))
else:
    print(2*(a + b) - 1)