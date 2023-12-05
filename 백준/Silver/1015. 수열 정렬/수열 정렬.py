import sys


input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().strip().split()))
length = len(A)
B = [0 for _ in range(length)]
sort_num = sorted(set(A))
rank = 0
for num in sort_num:
    for idx in list(filter(lambda x: A[x] == num, range(length))):
        B[idx] = rank
        rank += 1
print(' '.join(map(str, B)))
