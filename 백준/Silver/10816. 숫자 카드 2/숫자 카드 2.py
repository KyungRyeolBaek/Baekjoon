import sys


input = sys.stdin.readline
N = int(input())
have_cards = list(map(int, input().strip().split()))
cards_dict = {}
for card in have_cards:
    cards_dict[card] = cards_dict.get(card, 0) + 1

M = int(input())
find_cards = list(map(int, input().strip().split()))
result = []
for card in find_cards:
    result.append(str(cards_dict.get(card, 0)))

print(' '.join(result))