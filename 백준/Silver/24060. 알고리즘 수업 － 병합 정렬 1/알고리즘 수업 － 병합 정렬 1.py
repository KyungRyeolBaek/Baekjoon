import sys


class Merge_Sort:
    def __init__(self, K):
        self.count = 0
        self.k = K
        self.result = 0

    def merge_sort(self, A, p, r):
        # A[p..r]을 오름차순 정렬한다.
        if p < r:
            q = (p + r) // 2  # q는 p, r의 중간 지점
            self.merge_sort(A, p, q)  # 전반부 정렬
            self.merge_sort(A, q + 1, r)  # 후반부 정렬
            self.merge(A, p, q, r)  # 병합

    def merge(self, A, p, q, r):
        # A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
        # A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.
        i = p
        j = q + 1
        t = 0
        tmp = [0] * (r - p + 1)
        
        while i <= q and j <= r:
            if A[i] <= A[j]:
                tmp[t] = A[i]
                i += 1
            else:
                tmp[t] = A[j]
                j += 1
            t += 1
        
        while i <= q:  # 왼쪽 배열 부분이 남은 경우
            tmp[t] = A[i]
            i += 1
            t += 1
        
        while j <= r:  # 오른쪽 배열 부분이 남은 경우
            tmp[t] = A[j]
            j += 1
            t += 1
        
        for i in range(p, r + 1):
            A[i] = tmp[i - p]
            self.save_result(tmp[i - p])

    def save_result(self, result):
        self.count += 1
        if self.count == self.k:
            self.result = result


input = sys.stdin.readline
size, K = map(int, input().strip().split())
A = list(map(int, input().strip().split()))

Merge_Sort_ = Merge_Sort(K)
Merge_Sort_.merge_sort(A, 0, len(A) - 1)
if Merge_Sort_.result != 0:
    print(Merge_Sort_.result)
else:
    print(-1)