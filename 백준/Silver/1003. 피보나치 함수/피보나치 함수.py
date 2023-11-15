import sys


def fibonacci(n):
    return int(((1 + 5**0.5)**n - (1 - 5**0.5)**n) / ((2**n) * (5**0.5)))


n = int(sys.stdin.readline())
datas = [int(sys.stdin.readline().strip()) for _ in range(n)]    

for data in datas:
    result = [fibonacci(abs(data - 1)), fibonacci(data)]
    print('{} {}'.format(*result))