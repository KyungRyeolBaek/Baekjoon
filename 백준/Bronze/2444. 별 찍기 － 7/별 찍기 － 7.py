import sys


input = sys.stdin.readline
N = int(input().strip())
for n in range(2*N - 1):
    b = abs(N-1-n)
    print(' '*b + '*' + '*'*(2*(N - 1 - b)))