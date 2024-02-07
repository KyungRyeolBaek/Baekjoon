import sys


input = sys.stdin.readline
value = input().strip()
while value != "0 0":
    A, B = map(int, value.split())
    if A == 0 or B == 0:
        break
    if B % A == 0:
        print("factor")
    elif A % B == 0:
        print("multiple")
    else:
        print("neither")
    value = input().strip()