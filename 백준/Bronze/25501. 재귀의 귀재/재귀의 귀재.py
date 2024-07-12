import sys


class Palindrome:
    def __init__(self):
        self.count = 0

    def recursion(self, s, l, r):
        self.count += 1
        if l >= r: return 1
        elif s[l] != s[r]: return 0
        else: return self.recursion(s, l+1, r-1)

    def isPalindrome(self, s):
        return self.recursion(s, 0, len(s)-1)


input = sys.stdin.readline
N = int(input())
for _ in range(N):
    Palindrome_ = Palindrome()
    result = Palindrome_.isPalindrome(input().strip())
    print(result, Palindrome_.count)

