import sys


input = sys.stdin.readline
N = int(input())
stay_members = {}
for _ in range(N):
    event = input().strip().split()
    if event[1] == 'enter':
        stay_members[event[0]] = True
    else:
        del stay_members[event[0]]

members = sorted(stay_members.keys(), reverse=True)
for member in members:
    print(member)