import sys


input = sys.stdin.readline
N = int(input())
answer = [0 for _ in range(N)]
mapping = {}
numbers = list(map(int, input().strip().split()))
for idx, number in enumerate(numbers):
    idx_list = mapping.get(number, [])
    idx_list.append(idx)
    mapping[number] = idx_list

numbers = list(set(numbers))
numbers.sort()
count = 0
for number in numbers:
    for idx in mapping[number]:
        answer[idx] = str(count)
    count += 1

print(' '.join(answer))