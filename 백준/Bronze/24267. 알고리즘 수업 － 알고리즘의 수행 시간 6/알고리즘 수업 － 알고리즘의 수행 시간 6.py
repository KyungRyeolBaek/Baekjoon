import sys


def MenOfPassion(n, count=0, bigO=0):
    sum = 0
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            for k in range(j + 1, n + 1):
                sum += i * j * k
                count += 1
    bigO += 2
    return sum, count, bigO


input = sys.stdin.readline
n = int(input().strip())
count = sum([i * (i + 1) // 2 for i in range(1, n - 1)])
print(count)
print(3)
