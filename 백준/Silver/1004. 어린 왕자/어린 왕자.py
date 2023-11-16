import sys


input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    count = 0
    x1, y1, x2, y2 = list(map(int, input().strip().split()))
    n = int(input().strip())
    C = [list(map(int, input().strip().split())) for _ in range(n)]

    for cx, cy, r in C:
        distance_1 = ((x1 - cx)**2 + (y1 - cy)**2)**0.5
        distance_2 = ((x2 - cx)**2 + (y2 - cy)**2)**0.5

        if r > distance_1 and r > distance_2:
            pass
        elif r > distance_1:
            count += 1
        elif r > distance_2:
            count += 1

    print(count)
