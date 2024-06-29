import sys


input = sys.stdin.readline
N, M = map(int, input().strip().split())
words = dict()
for _ in range(N):
    word = input().strip()
    if len(word) >= M:
        words[word] = words.get(word, 0) + 1

words = sorted(words.items(), key=lambda x: (-1*x[1], -1*len(x[0]), x[0]))
for key, value in words:
    print(key)
