import sys


input = sys.stdin.readline
N, M = map(int, input().strip().split())
pocket_num_dict = {}
pocket_name_dict = {}
for idx in range(N):
    mon = input().strip()
    pocket_num_dict[idx + 1] = mon
    pocket_name_dict[mon] = idx + 1

answer = []
for _ in range(M):
    question = input().strip()
    if question.isnumeric():
        answer.append(pocket_num_dict[int(question)])
    else:
        answer.append(pocket_name_dict[question])

for ans in answer:
    print(ans)