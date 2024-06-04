import sys


input = sys.stdin.readline
N = int(input())
balloon = list(map(int, input().strip().split()))
idx = 0
count = balloon[idx]
idxs = [str(idx + 1)]
balloon[idx] = 0
# 풍선이 남지 않으면 종료한다.
while sum(balloon) != 0:
    if count > 0:
        while count != 0:
            idx += 1
            if balloon[idx % N] == 0:
                continue
            else:
                count -= 1
    elif count < 0:
        while count != 0:
            idx -= 1
            if balloon[idx % N] == 0:
                continue
            else:
                count += 1
    
    count = balloon[idx % N]
    balloon[idx % N] = 0
    idx = idx % N
    idxs.append(str((idx % N) + 1))
print(' '.join(idxs))