import sys


input = sys.stdin.readline
K = int(input().strip())
money = []
for _ in range(K):
    M = int(input().strip())
    if M == 0:
        money.pop()
    else:
        money.append(M)
print(sum(money))