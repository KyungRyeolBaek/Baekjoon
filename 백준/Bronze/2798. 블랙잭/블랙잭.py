import sys
from itertools import combinations


input = sys.stdin.readline
N, M = map(int, input().strip().split())
numbers = list(map(int, input().strip().split()))
combi = combinations(numbers, 3)
max_value = 0
for com in combi:
    value = sum(com)
    if value <= M and max_value < value:
        max_value = value
print(max_value)
