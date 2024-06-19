import sys


def gcd(x, y):
    while y:
	    x, y = y, x % y
    return x


input = sys.stdin.readline
N = input()
A = list(map(int, input().strip().split()))
s = A[-1]
min_num = s
for a in A[:-1]:
    num = gcd(s, a)
    if num < min_num:
        min_num = num
    s = s * a // num
if len(A) == 0:
    print(s**2)
elif s in A:
    print(s * min_num)
else:
    print(s)