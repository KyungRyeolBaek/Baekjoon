import sys


input = sys.stdin.readline
S = input().strip()
set_S = set(S)
dict_S = {}
for A in set_S:
    dict_S[A] = [1 if s == A else 0 for s in S]

N = int(input())
for _ in range(N):
    a, l, r = input().strip().split()
    l, r = map(int, [l, r])
    if a in dict_S:
        print(sum(dict_S[a][l:r + 1]))
    else:
        print(0)