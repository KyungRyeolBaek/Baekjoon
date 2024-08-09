import sys


input = sys.stdin.readline
N, M = map(int, input().strip().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().strip().split())))

presum_matirx = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        presum_matirx[i][j] = matrix[i - 1][j - 1] + presum_matirx[i][j - 1] + presum_matirx[i - 1][j] - presum_matirx[i - 1][j - 1] 

for _ in range(M):
    answer = 0
    x1, y1, x2, y2 = map(int, input().strip().split())
    answer = presum_matirx[x2][y2] - presum_matirx[x2][y1 - 1] - presum_matirx[x1 - 1][y2] + presum_matirx[x1 - 1][y1 - 1]
    print(answer)