import sys


input = sys.stdin.readline
N = int(input())
files = [input().strip() for _ in range(N)]
file_len = len(files[0])
answer = ''
for idx in range(file_len):
    string = files[0][idx]
    for file in files[1:]:
        if file[idx] != string:
            answer += '?'
            break
    else:
        answer += string

print(answer)