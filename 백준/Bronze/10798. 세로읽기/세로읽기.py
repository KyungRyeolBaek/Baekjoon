import sys


input = sys.stdin.readline
string = []
max_line = 0
for _ in range(5):
    line = input().strip()
    string.append(line)
    if max_line < len(line):
        max_line = len(line)

replace_string = []
for line in string:
    if len(line) < max_line:
        line = line.ljust(max_line, '-')
    replace_string.append(line)

result = ''
for j in range(max_line):
    for i in range(5):
        s = replace_string[i][j]
        if s != '-':
            result += s
print(result)
