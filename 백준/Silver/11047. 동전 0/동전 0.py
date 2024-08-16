import sys


input = sys.stdin.readline
N, K = map(int, input().strip().split())
coins = [int(input()) for _ in range(N)]
result = 0
for coin in coins[::-1]:
    q, r = divmod(K, coin)
    result += q
    K = r
    if K == 0:
        break

print(result)