import sys


def count_F(idx, line):
    if idx % 2 == 0:
        return [line[i] for i in range(0, 8, 2)].count('F')
    else:
        return [line[i] for i in range(1, 8, 2)].count('F')


input = sys.stdin.readline
answer = 0
for idx in range(8):
    answer += count_F(idx, input().strip())

print(answer)
