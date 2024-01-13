import sys


input = sys.stdin.readline
N = int(input().strip())
score = list(map(int, input().strip().split()))
max_score = max(score)
average_score = sum(map(lambda x:x/max_score*100, score)) / N
print(average_score)