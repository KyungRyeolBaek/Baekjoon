import sys


input = sys.stdin.readline
square = []
count = 0
for _ in range(3):
    angle = int(input().strip())
    if angle in square:
        count += 1
    square.append(angle)
if sum(square) != 180:
    print('Error')
else:
    print(['Scalene', 'Isosceles', 'Equilateral'][count])
