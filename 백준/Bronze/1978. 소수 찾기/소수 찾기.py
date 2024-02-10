import sys
import math


def is_prime_number(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


input = sys.stdin.readline
N = int(input().strip())
result = 0
for num in map(int, input().strip().split()):
    if is_prime_number(num):
        result += 1
print(result)
