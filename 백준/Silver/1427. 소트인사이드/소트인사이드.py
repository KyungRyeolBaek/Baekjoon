import sys


input = sys.stdin.readline
values = list(input().strip())
print(''.join(sorted(values, reverse=True)))