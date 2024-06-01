import sys


input = sys.stdin.readline
N, K = map(int, input().strip().split())
nums = [n for n in range(1, N + 1)]
pop_list = []
pos = 0
while len(nums) != 0:
    if pos >= 0:
        pos = (pos + K) % len(nums) - 1
    else:
        pos = (pos + K) % len(nums)
    pop_list.append(str(nums[pos]))
    del nums[pos]
print(f"<{', '.join(pop_list)}>")
