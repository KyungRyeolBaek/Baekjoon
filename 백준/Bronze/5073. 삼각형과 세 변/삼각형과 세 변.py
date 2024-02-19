import sys


input = sys.stdin.readline
triangle = 1
while True:
    triangle = sorted(list(map(int, input().strip().split())))
    if triangle == [0, 0, 0]:
        break
    if triangle[2] >= sum(triangle[0:2]):
        print('Invalid')
    else:
        count = len(set(triangle))
        print(['Equilateral', 'Isosceles', 'Scalene'][count - 1])