import sys


def backtest(y, N, x_table, add_cross_table, sub_cross_table):
    if y == N:
        return 1
    
    result = 0

    for x in range(N):
        if x_table[x] or add_cross_table[x + y] or sub_cross_table[x - y]:
            continue
    
        x_table[x] = True
        add_cross_table[x + y] = True
        sub_cross_table[x - y] = True

        result += backtest(y + 1, N, x_table, add_cross_table, sub_cross_table)

        x_table[x] = False
        add_cross_table[x + y] = False
        sub_cross_table[x - y] = False

    return result


input = sys.stdin.readline
N = int(input())
x_table = [False] * N
add_cross_table = [False] * (2 * N)
sub_cross_table = [False] * (2 * N)

print(backtest(0, N, x_table, add_cross_table, sub_cross_table))