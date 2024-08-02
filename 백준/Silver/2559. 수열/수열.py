import sys


input = sys.stdin.readline
N, K = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))
num = sum(nums[:K])
max_num = num
for i in range(N - K):
    num -= nums[i]
    num += nums[i + K]
    if max_num < num:
        max_num = num

print(max_num)