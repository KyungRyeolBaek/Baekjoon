import sys


input = sys.stdin.readline
N = int(input())
densers = set()
for _ in range(N):
    persons = input().strip().split()
    if len(densers) == 0:
        if 'ChongChong' in persons:
            for person in persons:
                densers.add(person)
    else:
        check = 0
        for person in persons:
            if person in densers:
                check = 1
        if check == 1:
            for person in persons:
                densers.add(person)
print(len(densers))
