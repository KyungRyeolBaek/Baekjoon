import sys


input = sys.stdin.readline
N = int(input().strip())
A = set(map(int, input().split()))
M = int(input().strip())
B = list(map(int, input().split()))

for i in B:
    if i in A:
        print(1)
    else:
        print(0)
