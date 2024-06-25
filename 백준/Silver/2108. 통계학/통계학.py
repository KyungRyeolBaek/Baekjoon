import sys
from collections import Counter


input = sys.stdin.readline
N = int(input())
nums = []
for _ in range(N):
    num = int(input().strip())
    nums.append(num)

print(int(round(sum(nums) / N, 0)))
print(sorted(nums)[N // 2])
counters = Counter(nums).most_common()
sorted_counters = sorted([num for num, count in counters if count == counters[0][1]])
if len(sorted_counters) == 1:
    print(sorted_counters[0])
else:
    print(sorted_counters[1])
print(max(nums) - min(nums))