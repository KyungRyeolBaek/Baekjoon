import sys


input = sys.stdin.readline

A, B = map(int, input().strip().split())
C = int(input().strip())

hour, minute = divmod((B + C), 60)
end_hour = (A + hour) % 24
print(end_hour, minute)
