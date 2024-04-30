import sys
import math


# 소수 판별 함수
def is_prime_number(x):
    if x < 2:
        return False    # 2 이하 소수 아님
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False    # 소수가 아님
    return True     # 소수임


input = sys.stdin.readline
M, N = map(int, input().strip().split())
for num in range(M, N + 1):
    if is_prime_number(num):
        print(num)
