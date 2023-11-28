import sys


input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x, y = map(int, input().strip().split())
    v = y - x
    h_v = int(v ** 0.5)
    if v == h_v**2:
        print(2 * h_v - 1)
    elif (v - h_v**2) <= h_v:
        print(2 * h_v)
    else:
        print(2 * h_v + 1)
