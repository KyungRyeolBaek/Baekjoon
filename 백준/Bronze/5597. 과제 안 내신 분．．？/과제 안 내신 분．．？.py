import sys


input = sys.stdin.readline
num = [i + 1 for i in range(30)]
for _ in range(28):
    num.remove(int(input().strip()))
for n in num:
    print(n)