'''
5
8 3 7 9 2
3
5 7 9

no yes yes
'''

import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

# array에 request가 있는지 없는지 확인
m = int(input())
request = list(map(int, input().split()))

array.sort()

for i in range(m):
    if request[i] in array:
        print("yes", end=' ')
    else:
        print("no", end=' ')

###########################################################################

# 이진 탐색
def binary_search(array, target, start, end):
    if start > end:
        return None

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

n = int(input())
array = list(map(int, input().split()))
array.sort()

# array에 request가 있는지 없는지 확인
m = int(input())
request = list(map(int, input().split()))

for i in request:
    res = binary_search(array, i, 0, n-1)

    if res != None:
        print("yes", end=' ')
    else:
        print("no", end=' ')

###########################################################################

# 계수 정렬

n = int(input())
array = [0] * 100001

# 0으로 초기화한 배열에 입력값으로 들어온 인덱스 값에 1을 추가
for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print("yes", end= ' ')
    else:
        print("no", end = ' ')