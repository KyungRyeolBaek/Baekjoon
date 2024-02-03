import sys


input = sys.stdin.readline
N = int(input().strip())
line = 0
while N > 0:
    line += 1
    N -= line

num = [n for n in range(1, line + 1)]
if line % 2:
    result = str(num[-N]) + '/' + str(num[line + N - 1])
else:
    result = str(num[line + N - 1]) + '/' + str(num[-N])
print(result)
