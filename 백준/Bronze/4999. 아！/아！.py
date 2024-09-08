import sys


input = sys.stdin.readline
a = input().strip()
b = input().strip()
if b in a:
    print('go')
else:
    print('no')