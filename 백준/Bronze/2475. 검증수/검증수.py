import sys


input = sys.stdin.readline

print(sum([num**2 for num in map(int, input().strip().split())]) % 10)