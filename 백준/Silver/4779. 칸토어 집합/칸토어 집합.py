import sys


def cantor(s):
    s = s + len(s) * ' ' + s
    return s


input = sys.stdin.readline
while True:
    s = '-'
    try:
        N = int(input())
        for _ in range(N):
            s = cantor(s)
        print(s)

    except:
        break