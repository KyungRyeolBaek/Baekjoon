import sys


input = sys.stdin.readline
N = int(input().strip())
x = 2
if N != 0:
    for n in range(N):
        x += 2**n
print(x ** 2)