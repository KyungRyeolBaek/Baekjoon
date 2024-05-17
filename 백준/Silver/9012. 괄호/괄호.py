import sys


def is_balenced(string):
    stack = []
    parenthesis_string = {')': '('}
    
    for char in string:
        p_s_keys = parenthesis_string.keys()
        p_s_values = parenthesis_string.values()
        if char in p_s_keys:
            if not stack or parenthesis_string[char] != stack.pop():
                return 'NO'
        elif char in p_s_values:
            stack.append(char)
    if stack:
        return 'NO'
    else:
        return 'YES'


input = sys.stdin.readline
T = int(input())
for _ in range(T):
    string = input().strip()
    print(is_balenced(string))