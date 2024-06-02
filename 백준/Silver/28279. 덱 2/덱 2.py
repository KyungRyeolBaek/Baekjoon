import sys
from collections import deque


input = sys.stdin.readline
N = int(input())
que = deque()
for _ in range(N):
    command = input().strip()
    if command == '3':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif command == '4':
        if que:
            print(que.pop())
        else:
            print(-1)
    elif command == '5':
        print(len(que))
    elif command == '6':
        if que:
            print(0)
        else:
            print(1)
    elif command == '7':
        if que:
            print(que[0])
        else:
            print(-1)
    elif command == '8':
        if que:
            print(que[-1])
        else:
            print(-1)
    else:
        command, num = command.split()
        if command == '1':
            que.appendleft(num)
        elif command == '2':
            que.append(num)
