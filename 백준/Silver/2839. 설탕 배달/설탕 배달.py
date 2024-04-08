import sys


input = sys.stdin.readline
N = int(input())
a = N // 5
count = 0
while a >= 0:
    b, c = divmod(N - (a * 5), 3)
    if c == 0:
        break
    else:
        a -= 1
if a + b == 0 or c != 0:
    print(-1)
else:
    print(a + b)