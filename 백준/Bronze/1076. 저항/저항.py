import sys


input = sys.stdin.readline
dictionary = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}
result = 0
for i in range(3):
    color = input().strip()
    if i == 0:
        result += dictionary[color] * 10
    elif i == 1:
        result += dictionary[color]
    else:
        result *= 10 ** dictionary[color]

print(result)