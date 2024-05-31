import sys
from collections import deque


input = sys.stdin.readline
N = int(input())
cards = deque([n + 1 for n in range(N)])
count = 0
while len(cards) != 1:
    if count % 2 == 0:
        cards.popleft()
    else:
        cards.append(cards.popleft())
    count += 1
print(cards[0])
