import sys


input = sys.stdin.readline
num_list = []
for _ in range(10):
    num = int(input().strip()) % 42
    if num not in num_list:
        num_list.append(num)

print(len(num_list))