import sys


input = sys.stdin.readline
numbers = list(map(int, input().strip().split()))

big = 0
count = {}
for number in numbers:
    if number > big:
        big = number
    if number in count:
        count[number] += 1
    else:
        count[number] = 1

same_number = max(count, key=count.get)
if len(count) == 1:
    print(10000 + same_number * 1000)
elif len(count) == 2:
    print(1000 + same_number * 100)
else:
    print(big * 100)