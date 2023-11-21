import sys
import math


input = sys.stdin.readline

N = int(input())
F = int(input())

N = math.floor(N / 100) * 100
if (N % F) == 0:
    print('00')
else:
    result = str(((N // F) + 1) * F)[-2:]
    print(result)