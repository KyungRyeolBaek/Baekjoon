import sys


n = int(sys.stdin.readline())
datas = [sys.stdin.readline().strip() for _ in range(n)]

for data in datas:
    data = list(map(int, data.split()))
    x1, y1, r1, x2, y2, r2 = data
    d = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    if (x1, y1, r1) == (x2, y2, r2):
        print(-1)
    elif (r1 + r2 < d) or (abs(r1 - r2) > d) or (d == 0 and r1 != r2):
        print(0)
    elif (r1 + r2 == d) or abs(r1 - r2) == d:
        print(1)
    elif abs(r1 - r2) < d < (r1 + r2):
        print(2)