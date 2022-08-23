# 두 배열의 원소 교체
# 첫 번째 배열의 합이 최대가 되도록
'''
<고려할점>
1. k번만 바꿀 수 있다.
2. 2번째 배열에서 해당 인덱스 값의 크기가 1번째 배열의 해당 인덱스 값과 비교
3. 1번째 원소의 크기가 2번째 원소보다 크거나 같을 때는 무시???

5 5
2 4 4 5 6
5 5 6 6 5
'''

import sys

input = sys.stdin.readline

# n == 원소, k == 바꿀 수 있는 횟수
n, k = map(int, input().split())

array_data = [list(map(int, input().split())) for _ in range(2)]

# 배열 A의 오름차순 정렬 후 앞에서 부터 변경
# 배열 B의 내림차순 정렬 후 개수 파악
array_data[0].sort()
array_data[1].sort(reverse=True)

# k 횟수만큼 변경
# 문제점
# - 두 배열의 해당 인덱스 값과 비교하고 바꿔줘야함 
for i in range(n):
    if k == 0:
        break

    array_data[0][i] = array_data[1][i]
    '''
    # + 조건
    if array_data[0][i] < array_data[1][i]:
        array_data[0][i] = array_data[1][i]
    '''
    k -= 1

print(sum(array_data[0]))

##################################################################

n, k = map(int, input().split()) 
a = list(map(int, input().split())) 
b = list(map(int, input().split())) 

a.sort() 
b.sort(reverse=True) 

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i]:
        # 두 원소를 교체
        a[i], b[i] = b[i], a[i]
    else: # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
        break

print(sum(a)) # 배열 A의 모든 원소의 합을 출력
