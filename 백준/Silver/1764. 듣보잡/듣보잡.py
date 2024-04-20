import sys


input =sys.stdin.readline
N, M = map(int, input().strip().split())
none_hear = {input().strip(): True for _ in range(N)}
none_see = {input().strip(): True for _ in range(M)}
none_hear_see = []
if len(none_hear) <= len(none_see):
    for person in none_hear:
        if none_see.get(person, False) == True:
            none_hear_see.append(person)
else:
    for person in none_see:
        if none_hear.get(person, False) == True:
            none_hear_see.append(person)

none_hear_see.sort()
print(len(none_hear_see))
for person in none_hear_see:
    print(person)