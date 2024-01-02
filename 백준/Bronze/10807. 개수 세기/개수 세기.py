import sys


input = sys.stdin.readline
N = int(input().strip())
print(list(map(int, input().strip().split())).count(int(input().strip())))
