import sys


def stars(star, start, end):
    if start > end:
        return star

    triple_star = ''
    mid_star = ''
    for line in star.split('\n'):
        triple_star += line * 3 + '\n'
        mid_star += line + (len(line) * ' ') + line + '\n'
    
    return_star = triple_star + mid_star + triple_star.rstrip()
    return stars(return_star, start + 1, end)


input = sys.stdin.readline
N = int(input().strip())
n = 1
while True:
    if 3 ** n >= N:
        break
    else:
        n += 1
star = stars('*', 1, n)
print(star)