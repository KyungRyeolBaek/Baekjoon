import sys
import itertools


input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    P = []
    total_x, total_y = 0, 0
    for _ in range(N):
        x, y = map(int, input().strip().split())
        total_x += x
        total_y += y
        P.append((x, y))

    result = 10**10
    combi = list(itertools.combinations(P, N // 2))
    for combi_P in combi:
        half_x1, half_y1 = 0, 0
        for x, y in combi_P:
            half_x1 += x
            half_y1 += y

        half_x2 = total_x - half_x1
        half_y2 = total_y - half_y1

        vector = ((half_x1 - half_x2)**2 + (half_y1 - half_y2)**2)**0.5
        result = min(result, vector)

    print(result)
