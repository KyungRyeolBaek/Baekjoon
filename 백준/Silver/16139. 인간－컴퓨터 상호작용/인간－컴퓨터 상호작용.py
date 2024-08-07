import sys


input = sys.stdin.readline
S = input().rstrip()
dict_S = {chr(s): [0] * (len(S) + 1) for s in range(97, 123)}
for i in range(len(S)):
    for char in dict_S:
        dict_S[char][i + 1] = dict_S[char][i]
    dict_S[S[i]][i + 1] += 1

N = int(input())
for _ in range(N):
    a, l, r = input().rstrip().split()
    l, r = map(int, [l, r])
    print(dict_S[a][r + 1] - dict_S[a][l])