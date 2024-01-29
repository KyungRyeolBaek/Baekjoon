import sys


input = sys.stdin.readline
N, B = map(int, input().strip().split())
dic = {10 + idx: chr(i) for idx, i in enumerate(range(ord('A'), ord('Z') + 1))}
result = ''
while N:
    N, b = divmod(N, B)
    if b >= 10:
        b = dic[b]
    result += str(b)
print(result[::-1])