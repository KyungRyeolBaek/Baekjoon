import sys


input = sys.stdin.readline
N = int(input().strip())
count = 1
N -= 1
while N > 0:
    N -= 6 * count
    count += 1

print(count)
