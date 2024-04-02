import sys


input = sys.stdin.readline
N, M = map(int, input().strip().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().strip().replace('B', '1').replace('W', '0'))))

filter_lines = [[0 if i % 2 == 0 else 1 for i in range(M)], [1 if i % 2 == 0 else 0 for i in range(M)]]
max_count = 2500
filter_height = N - 8 + 1
filter_weight = M - 8 + 1
for height in range(filter_height):
    for weight in range(filter_weight):
        for filter_count in range(2):
            count = 0
            for idx, line in enumerate(board[height:height + 8]):
                if (filter_count + idx) % 2 == 0:
                    select = 0
                else:
                    select = 1
                for value, filter_value in zip(line[weight:weight + 8], filter_lines[select][weight:weight + 8]):
                    count += abs(value - filter_value)

            if max_count > count:
                max_count = count

print(max_count)
