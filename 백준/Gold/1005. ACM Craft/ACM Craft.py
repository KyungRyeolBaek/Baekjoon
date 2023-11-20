import sys
from collections import deque


input = sys.stdin.readline

# T: 테스트 케이스
# N, K: 건물 개수, 건물 순서 규칙 총 개수
# D: 걸리는 시간
# X, Y: 건물 순서.
T = int(input())
for _ in range(T):
    N, K = map(int, input().strip().split())
    D = list(map(int, input().strip().split()))
    G = [[] for _ in range(N + 1)]
    require_building_count = [0] * (N + 1)
    for _ in range(K):
        X, Y = map(int, input().strip().split())
        G[X].append(Y)
        require_building_count[Y] += 1
    W = int(input())

    # 건물을 짓는데 걸리는 최소 시간을 저장하는 배열
    time_to_build = [0] * (N + 1)

    # 짓기 시작할 건물을 큐에 추가
    que = deque([])
    for i in range(1, N + 1):
        if require_building_count[i] == 0:
            que.append(i)
            time_to_build[i] = D[i - 1]

    while que:
        current_building = que.popleft()
        if current_building == W:
            print(time_to_build[current_building])
            break
        for next_building in G[current_building]:
            require_building_count[next_building] -= 1
            # 소요 시간 최대값으로.
            time_to_build[next_building] = max(time_to_build[next_building], time_to_build[current_building] + D[next_building - 1])
            if require_building_count[next_building] == 0:
                que.append(next_building)
