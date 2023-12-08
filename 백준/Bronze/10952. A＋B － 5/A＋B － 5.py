import sys


input = sys.stdin.readline

while True:
    A, B = map(int, input().strip().split())
    if (A and B) != 0:
        print(A + B)
    else:
        break
