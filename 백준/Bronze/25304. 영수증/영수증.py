import sys


input = sys.stdin.readline

X = int(input().strip())
N = int(input().strip())
for _ in range(N):
    a, b = map(int, input().strip().split())
    X -= (a * b)

if X:
    print('No')
else:
    print('Yes')
