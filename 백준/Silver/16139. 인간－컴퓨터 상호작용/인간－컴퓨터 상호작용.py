import sys


input = sys.stdin.readline
S = input().strip()
N = int(input())
for _ in range(N):
    a, l, r = input().strip().split()
    l, r = map(int, [l, r])
    print(S[l:r + 1].count(a))