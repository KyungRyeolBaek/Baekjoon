import sys


def is_balenced(string):
    stack = []
    parenthesis_string = {')': '(', ']': '['}
    
    for char in string:
        p_s_keys = parenthesis_string.keys()
        p_s_values = parenthesis_string.values()
        if char in p_s_keys:
            if not stack or parenthesis_string[char] != stack.pop():
                return 'no'
        elif char in p_s_values:
            stack.append(char)
    if stack:
        return 'no'
    else:
        return 'yes'


input = sys.stdin.readline
while True:
    string = input().rstrip()
    if string == '.':
        break
    print(is_balenced(string))