import sys


def factor(num1, num2):
    if num2 == 0:
        return num1
    else:
        return factor(num2, num1 % num2)  # 유클리드 호제법 사용


input = sys.stdin.readline
N = int(input())
for _ in range(N):
    A, B = map(int, input().strip().split())
    print(int(A * B / factor(A, B)))