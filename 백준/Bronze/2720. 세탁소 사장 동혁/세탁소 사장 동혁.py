import sys


input = sys.stdin.readline
N = int(input().strip())
money = [25, 10, 5, 1]
result = []
for _ in range(N):
    answer = []
    C = int(input().strip())
    for m in money:
        a, C = divmod(C, m)
        answer.append(str(a))
    result.append(answer)
for r in result:
    print(' '.join(r))