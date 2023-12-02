import sys


def DPS(graph, x, y):
    if graph[y][x] == 1:
        graph[y][x] = 0
        if x - 1 >= 0:
            DPS(graph, x - 1, y)
        if y - 1 >= 0:
            DPS(graph, x, y - 1)
        if x <= M - 2:
            DPS(graph, x + 1, y)
        if y <= N - 2:
            DPS(graph, x, y + 1)
    return graph


sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    M, N, K = map(int, input().strip().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    point = []
    for _ in range(K):
        x, y = map(int, input().strip().split())
        graph[y][x] = 1
        point.append((x, y))

    count = 0
    for x, y in point:
        if graph[y][x] == 1:
            count += 1
            graph = DPS(graph, x, y)

    print(count)
