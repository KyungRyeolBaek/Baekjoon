import sys


input = sys.stdin.readline
a1, a0 = map(int, input().strip().split())
c = int(input().strip())
n0 = int(input().strip())

if (c - a1) * n0 >= a0 and a1 <= c:
    print(1)
else:
    print(0)