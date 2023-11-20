import sys


input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    answer = ((a % 10) ** (b % 4 + 4)) % 10
    if answer == 0:
        print(10)
    else:
        print(answer)
