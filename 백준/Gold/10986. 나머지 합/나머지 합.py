import sys


def count_subarrays_with_remainder(M, array):
    # 누적 합의 나머지를 저장할 카운터 배열
    remainder_count = [0] * M
    remainder_count[0] = 1  # 초기 상태를 위해 나머지 0인 경우 하나 추가
    
    prefix_sum = 0
    result = 0

    for num in array:
        prefix_sum += num
        remainder = prefix_sum % M
        
        # 이 나머지가 나온 적이 있는지 확인하고 결과에 추가
        result += remainder_count[remainder]
        
        # 현재 나머지 카운트를 증가
        remainder_count[remainder] += 1
    
    return result

# 입력
input = sys.stdin.readline
N, M = map(int, input().split())
array = list(map(int, input().split()))

# 결과 계산 및 출력
print(count_subarrays_with_remainder(M, array))