import sys


input = sys.stdin.readline
N = input()
num = list(map(int, input().strip().split()))
print(min(num), max(num))