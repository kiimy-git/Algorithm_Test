# 구간 합
'''
1. N개의 수에 대하여 접두사 합(Prefix Sum)을 계산하여 배열 P에 저장
2. 매 M개의 쿼리 정보 [L, R]을 확인할 때, 구간 합은 P[R] - P[L-1]
'''

n = 5
data = [10, 20, 30, 40, 50]

# 1 - 3번째, 60
# 2 - 5번째, 140
# 3 - 4번째, 70

sum_value = 0
# 구간 합 리스트
# 0 을 넣어주는 이유 left -1 => list error
prefix_sum = [0]

for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

# data index
left = 1
right = 3
print(data)
print(prefix_sum)
print(prefix_sum[right] - prefix_sum[left - 1])