import sys


def hanoi(n, from_pos, to_pos, aux_pos):
    global count, moves
    if n == 1:
        count += 1
        moves.append(f'{from_pos} {to_pos}')
        return count
    hanoi(n - 1, from_pos, aux_pos, to_pos)
    count +=1
    moves.append(f'{from_pos} {to_pos}')
    hanoi(n - 1, aux_pos, to_pos, from_pos)
    return count


count = 0
moves = []
input = sys.stdin.readline
print(hanoi(int(input().strip()), 1, 3, 2))
for move in moves:
    print(move)
