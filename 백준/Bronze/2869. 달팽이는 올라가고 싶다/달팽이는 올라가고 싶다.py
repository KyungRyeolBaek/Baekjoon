import sys
import math


imput = sys.stdin.readline
A, B, V = map(int, input().strip().split())
day = (V - B) / (A - B)
print(math.ceil(day))
