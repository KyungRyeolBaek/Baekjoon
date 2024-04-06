import sys


input = sys.stdin.readline
N = int(input())
result = 0
num = 666
while N > 0:
    count = 0
    last_num = 0
    for n in str(num):
        if n == '6':
            if last_num == '6':
                count += 1
            else:
                count = 1
        else:
            count = 0
        if count >= 3:
            N -= 1
            result = num
            break
        last_num = str(n)
    num +=1
print(result)