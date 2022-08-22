array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
'''
1. 가장 큰 데이터가 9, 가장 작은 데이터가 0
2. 정렬해야할 데이터의 범위는 0-9, 리스트의 인덱스가 모든 범위를 포함할 수 있도록 한다.
3. 즉, 단순히 크기가 10인 리스트를 선언
4. 처음에는 리스트의 모든 데이터가 0이 되도록 초기화
5. 데이터를 하나씩 확인하며 데이터의 값과 동일한 인덱스의 데이터를 1씩 증가시키면 계수 정렬 완료
6. 결과적으로 각 데이터가 몇 번 등장했는지 그 횟수가 기록됨
'''

# max, min
max_value = max(array)
min_value = min(array)

# 정렬 데이터 리스트 개수 및 0으로 초기화
count_list = []

for i in range(min_value, max_value+1):
    count_list.append(0)

# 데이터와 count_list 인덱스 값과 일치하면 인덱스의 데이터를 + 1
for i in array:
    if i <= len(count_list): # 굳이 필요없음...
        count_list[i] += 1

print(count_list)

# 각 인덱스 값에서 횟수만큼 출력
for i in range(len(count_list)):
    # count
    for j in range(count_list[i]):
        print(i, end=' ')

print()
###########################################################################

# == 최솟값이 0이라는 걸 알았을 때
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

# 이하 같음
for i in range(len(count_list)):
    # count
    for j in range(count_list[i]):
        print(i, end=' ')