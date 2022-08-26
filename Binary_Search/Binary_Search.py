# 이진 탐색
'''
10 4
0 2 4 6 8 10 12 14 16 18
3

10 7
1 3 5 7 9 11 13 15 17 19
4

10 7
1 3 5 6 9 11 13 15 17 19
원소가 존재하지 않습니다
'''

import sys

input = sys.stdin.readline

input_data = input().split()
n = int(input_data[0])
t = input_data[1]

# 정렬되있는 데이터
# 만약 list(map(int, input().split())) 이렇게 하면
# input_dat = map(int, input().split()) 하면 됨
array = input().split()

start_index = 0
end_index = n-1
middle_index = (start_index + end_index) // 2

start = array[start_index]
end = array[end_index]
middle = array[middle_index]

# 찾으려는 데이터와 middle과 비교
# 중간값이 target 값보다 크면 중간 index이후의 값은 확인할 필요가 없다
# => 끝점(n-1)을 중간점(middle_index - 1)로 옮긴다. = 반복되야하는 부분(재귀 함수)
# 그리고 다시 시작점과 끝점의 중간을 찾음
while True:

    if t < middle:
        end_index = middle_index - 1
        end = array[end_index]

        middle_index = (start_index + end_index) // 2
        middle = array[middle_index]

        

    elif t > middle:
        start_index = middle_index + 1
        start = array[start_index]

        middle_index = (start_index + end_index) // 2
        middle = array[middle_index]

        if middle == t:
            start_index += 1
            print(start_index)
            break

        elif t not in array:
            print("원소가 존재하지 않습니다")
            break


##############################################################################

# 재귀함수 활용

def binary_search(array, target, start, end):
    if start > end:
        return None

    # 중간값 설정
    mid = (start + end) // 2

    # 중간점이 찾고자 하는 값과 같을 경우 해당 값 출력
    if array[mid] == target:
        return mid
    
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 
    # 끝점을 중간점 - 1 이동
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)

    # 중간점의 값보다 찾고자 하는 값이 큰 경우
    # 시작점을 중간점 + 1 이동
    else:
        return binary_search(array, target, mid + 1, end)

num, target = map(int, input().split())  

array1 = list(map(int, input().split()))

res = binary_search(array1, target, 0, n-1)

if res == None:
    print("원소가 존재하지 않습니다")

else:
    print(res+1)

#####################################################################

# 단순하게 반복문 사용
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        # 중간점이 찾고자 하는 값과 같을 경우 해당 값 출력
        if array[mid] == target:
            return mid
        
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 
        # 끝점을 중간점 - 1 이동
        elif array[mid] > target:
            end = mid - 1

        # 중간점의 값보다 찾고자 하는 값이 큰 경우
        # 시작점을 중간점 + 1 이동
        else:
            start = mid + 1

    return None 

num, target = map(int, input().split())  

array1 = list(map(int, input().split()))

res = binary_search(array1, target, 0, n-1)

if res == None:
    print("원소가 존재하지 않습니다")

else:
    print(res+1)