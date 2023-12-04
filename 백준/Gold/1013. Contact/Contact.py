import re
import sys


input = sys.stdin.readline

T = int(input().strip())
for i in range(T):
    string = input().strip()
    pattern = re.compile('(100+1+|01)+')
    matching = pattern.fullmatch(string)
    if matching:
        print('YES')
    else:
        print('NO')
