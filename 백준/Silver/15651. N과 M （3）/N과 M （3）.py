import sys


input = sys.stdin.readline
N, M = map(int, input().strip().split())
results = ['1' for _ in range(M)]
print(' '.join(results))
while results != [f'{N}' for _ in range(M)]:
    cur = -1
    results[cur] = str(int(results[cur]) + 1)
    while True:
        if results[cur] == f'{N + 1}':
            results[cur] = '1'
            cur -= 1
            results[cur] = str(int(results[cur]) + 1)
        else:
            break
    print(' '.join(results))
