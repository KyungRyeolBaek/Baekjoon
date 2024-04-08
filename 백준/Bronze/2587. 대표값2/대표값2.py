import sys


input = sys.stdin.readline
values = []
for _ in range(5):
    values.append(int(input()))

print(int(sum(values) / len(values)))
values.sort()
print(values[len(values) // 2])
