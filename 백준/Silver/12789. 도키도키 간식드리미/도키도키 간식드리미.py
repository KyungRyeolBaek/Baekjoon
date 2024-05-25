import sys


input = sys.stdin.readline
N = int(input())
line = list(map(int, input().strip().split()))
sub_line = []
resive = [0]
while line or sub_line:
    curr_num = 0
    sub_num = 0
    next_num = resive[-1] + 1
    if line:
        curr_num = line[0]
    if sub_line:
        sub_num = sub_line[-1]
    if next_num == sub_num:
        resive.append(sub_line.pop())
    elif next_num == curr_num:
        resive.append(curr_num)
        del line[0]
    elif next_num != curr_num and curr_num != 0:
        sub_line.append(curr_num)
        del line[0]
    elif line == []:
        print('Sad')
        break

if line == [] and sub_line == []:
    print('Nice')