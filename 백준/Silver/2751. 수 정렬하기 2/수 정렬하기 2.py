import sys


input = sys.stdin.readline
N = int(input())
values = [int(input()) for _ in range(N)]
values.sort()
for value in values:
    print(value)