import sys


input = sys.stdin.readline
answer = ['-1' for _ in range(26)]
for idx, string in enumerate(input().strip()):
    pos = ord(string) - 97
    if answer[pos] == '-1':
        answer[pos] = str(idx)

print(' '.join(answer))