import sys


input = sys.stdin.readline
len_A, len_B = map(int, input().strip().split())
A = set(map(int, input().strip().split()))
B = set(map(int, input().strip().split()))

print(len(A - B) + len(B - A))