import sys


# 소수면 1 아니면 0, N 값까지의 소수 찾기.
def is_prime_list(N = 1000001):
    prime = []
    check = [1] * N
    check[0] = 0
    check[1] = 0

    for i in range(2, N):
        if check[i] == 1:
            prime.append(i)
            for j in range(2*i, N, i):
                check[j] = 0
    return prime, check

T = int(sys.stdin.readline())
prime, check = is_prime_list()
for _ in range(T):
    count = 0
    N = int(sys.stdin.readline())
    for i in prime:
        if i >= N:
            break
        if check[N - i] and i <= N - i:  # 순서만 다른거 counting 하지 않기 위해
            count += 1
    print(count)