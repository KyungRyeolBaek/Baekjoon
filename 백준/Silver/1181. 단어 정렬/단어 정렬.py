import sys


input = sys.stdin.readline
N = int(input())
string_list = set([])
for _ in range(N):
    string_list.add(input().strip())

string_list = list(string_list)
string_list.sort(key=lambda x: (len(x), x))
for string in string_list:
    print(string)