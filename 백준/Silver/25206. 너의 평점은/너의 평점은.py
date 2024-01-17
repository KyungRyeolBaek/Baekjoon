import sys


input = sys.stdin.readline
grade = {'A+': 4.5, 'A0': 4, 'B+': 3.5, 'B0':3, 'C+': 2.5, 'C0':2, 'D+': 1.5, 'D0': 1, 'F': 0}
score = 0
t_score = 0
for _ in range(20):
    _class, _time, _grade = input().strip().split()
    if _grade != 'P':
        score += float(_time) * grade[_grade]
        t_score += float(_time)
if score != 0:
    print(score / t_score)
else:
    print(0)