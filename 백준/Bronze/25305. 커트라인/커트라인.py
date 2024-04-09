import sys


input = sys.stdin.readline
N, k = map(int, input().strip().split())
x = list(map(int, input().strip().split()))
x.sort()
print(x[-k])
