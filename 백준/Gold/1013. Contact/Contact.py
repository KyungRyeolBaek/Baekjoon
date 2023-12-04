import re
import sys


input = sys.stdin.readline

T = int(input().strip())
for i in range(T):
    string = input().strip()
    pattern = '(100+1+|01)+'
    matching = re.fullmatch(pattern, string)
    if matching:
        print('YES')
    else:
        print('NO')
