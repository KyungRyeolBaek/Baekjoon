import sys


input = sys.stdin.readline
N, M = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))
num_sum = [0]
sum_all = 0
for num in nums:
    sum_all += num
    num_sum.append(sum_all)
for _ in range(M):
    i, j = map(int, input().strip().split())
    print(num_sum[j] - num_sum[i - 1])
