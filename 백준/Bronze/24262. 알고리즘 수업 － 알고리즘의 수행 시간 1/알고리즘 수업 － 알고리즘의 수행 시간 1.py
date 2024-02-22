import sys


input = sys.stdin.readline
n = int(input().strip())


def MenOfPassion(n, count=0, O=0):
    A = [n / 2]
    count += 1
    return A, count, O

A, count, O = MenOfPassion(n)
print(count)
print(O)