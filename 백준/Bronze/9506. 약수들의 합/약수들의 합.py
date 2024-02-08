import sys


input = sys.stdin.readline
while True:
    f = 1
    f_list = []
    n = int(input())
    if n == -1:
        break

    while n:
        if n % f == 0:
            f_list.append(f)
        f += 1
        if f >= n:
            break

    if sum(f_list) == n:
        print(str(n), '=', ' + '.join([str(f) for f in f_list]))
    else:
        print(str(n), 'is NOT perfect.')