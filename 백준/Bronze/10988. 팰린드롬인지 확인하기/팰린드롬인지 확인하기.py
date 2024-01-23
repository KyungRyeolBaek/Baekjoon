import sys


input = sys.stdin.readline
s = input().strip()
odd = len(s) % 2
half = len(s) // 2
if odd:
    if s[:half] == ''.join(list(reversed(s[half+1:]))):
        print(1)
    else:
        print(0)
else:
    if s[:half] == ''.join(list(reversed(s[half:]))):
        print(1)
    else:
        print(0)