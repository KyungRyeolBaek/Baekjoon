import sys


input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().strip().split())

A = [[a, b], [d, e]]
B = [[c], [f]]
A_inv = [A_b / (a*e - b*d) for A_m in [[e, -b], [-d, a]] for A_b in A_m]
x = c * A_inv[0] + f * A_inv[1]
y = c * A_inv[2] + f * A_inv[3]
print(' '.join(list(map(lambda x: str(round(x)), [x, y]))))
