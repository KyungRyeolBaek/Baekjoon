import sys


def MenOfPassion(N: int, count: int, degree: int) -> int:
    sum = 0
    degree += 1
    for i in range(1, N + 1):
        sum += i
        count += 1
    return sum, count, degree


input = sys.stdin.readline
_, count, degree = MenOfPassion(int(input().strip()), 0, 0)
print(count)
print(degree)
