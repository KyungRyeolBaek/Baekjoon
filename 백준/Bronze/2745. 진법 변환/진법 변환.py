import sys


input = sys.stdin.readline
N, B = input().strip().split()
dic = {chr(i): 10 + idx for idx, i in enumerate(range(ord('A'), ord('Z') + 1))}
result = 0
for idx, n in enumerate(N[::-1]):
    if n in dic: 
        n = dic[n]
    result += (int(B)**idx) * int(n)
print(result)