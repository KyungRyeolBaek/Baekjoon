import sys


input = sys.stdin.readline
N = int(input())
names = set()
count = 0
for _ in range(N):
    name = input().strip()
    if name != 'ENTER':
        names.add(name)
    else:
        count += len(names)
        names = set()
count += len(names)
print(count)