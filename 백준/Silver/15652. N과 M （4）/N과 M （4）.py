import sys


input = sys.stdin.readline
N, M = map(int, input().strip().split())
results = ['1' for _ in range(M)]
print(' '.join(results))
while results != [f'{N}' for _ in range(M)]:
    cur = -1
    results[cur] = str(int(results[cur]) + 1)
    while True:
        if results[cur] >= f'{N + 1}':
            if results[cur - 1] > f'{N}':
                results[cur] = str(int(results[cur - 1]))
            elif results[cur - 1] == f'{N}':
                i = 1
                while True:
                    if results[cur - 1 - i] == f'{N}':
                        i += 1
                    else:
                        results[cur] = str(int(results[cur - 1 - i]) + 1)
                        break
            else:
                results[cur] = str(int(results[cur - 1]) + 1)
            cur -= 1
            results[cur] = str(int(results[cur]) + 1)
        else:
            break
    print(' '.join(results))