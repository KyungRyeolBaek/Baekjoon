import sys


def factor(num1, num2):
    if num2 == 0:
        return num1
    else:
        return factor(num2, num1 % num2)  # 유클리드 호제법 사용


input = sys.stdin.readline
N = int(input())
sub = []
before = int(input())
for _ in range(N - 1):
    curr = int(input())
    sub.append(curr - before)
    before = curr

set_sub = set(sub)
fac = 0
for idx, s in enumerate(set_sub):
    if idx == 0:
        fac = s
    else:
        fac = factor(fac, s)

result = 0
for s in sub:
    result += s // fac - 1
print(result)