import sys


input = sys.stdin.readline

A = int(input().strip())
B = input().strip()

for b in B[::-1]:
    print(A * int(b))
print(A * int(B))
