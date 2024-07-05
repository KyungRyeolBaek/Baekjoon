import sys


def factorial(x):
    n = 1
    for i in range(1,x+1):
        n = n*i 
    return n


input = sys.stdin.readline
N = int(input().strip())
print(factorial(N))