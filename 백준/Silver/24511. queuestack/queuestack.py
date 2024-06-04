import sys
from collections import deque


input = sys.stdin.readline
N = int(input())
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))
M = int(input())
C = list(map(int, input().strip().split()))

result = []
que = deque([b for a, b in zip(A, B) if a == 0])
for c in C:
    que.appendleft(c)
    result.append(str(que.pop()))
print(' '.join(result))
