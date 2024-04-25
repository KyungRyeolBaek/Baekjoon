import sys


def factor(num1, num2):
    if num2 == 0:
        return num1
    else:
        return factor(num2, num1 % num2)  # 유클리드 호제법 사용


input = sys.stdin.readline
A, B = map(int, input().strip().split())
a, b = map(int, input().strip().split())
num1 = A * b + a * B
num2 = B * b

while factor(num1, num2) != 1:
    fac = factor(num1, num2)
    num1, num2 = int(num1 / fac), int(num2 / fac)

print(num1, num2)