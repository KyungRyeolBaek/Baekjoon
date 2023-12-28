import sys


input = sys.stdin.readline

N = int(input().strip())
print((N // 4) * 'long ' + 'int')