import sys


input = sys.stdin.readline

_min, _max = map(int, input().strip().split())
square = [s**2 for s in range(1, int(_max ** 0.5) + 1)]
set_square = set()
for s in square:
    if s != 1 and (s not in set_square):
        s_min = (_min // s) * s
        if s_min <= _max:
            mul = set([a for a in range(s_min, _max + 1, s) if (a >= _min) and (a not in set_square)])
            set_square |= mul
nono = _max - _min + 1 - len(set_square)
print(nono)
