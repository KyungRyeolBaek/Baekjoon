import sys


input = sys.stdin.readline
bowls = [int(input()) for _ in range(3)]
print(sorted(bowls)[1])