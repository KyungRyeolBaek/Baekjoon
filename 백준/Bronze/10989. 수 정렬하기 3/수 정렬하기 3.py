import sys


input = sys.stdin.readline
N = int(input())
values = {i: 0 for i in range(10001)}
for _ in range(N):
    values[int(input())] += 1
for i in range(10001):
    if values[i] != 0:
        for _ in range(values[i]):
            print(i)