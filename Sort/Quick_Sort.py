array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
p = array[0]


# 왼쪽에서부터 작은 숫자, 오른쪽에서부터 큰 숫자 찾음
left_list = []
right_list = []

left_list = [array[i] for i in range(1, len(array)) if array[i] <= p]
right_list = [array[i] for i in range(1, len(array)) if array[i] > p]

print(left_list +  [p] + right_list)

# left_list, right_list 반복 = 재귀 함수 사용

# python의 장점을 살린 퀵 정렬
def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면
    if len(array) <= 1:
        return array
    
    # 피벗 설정
    pivot = array[0]

    # 피벗을 제외한 array
    tail = array[1:]

    left_list = [i for i in tail if i <= pivot]
    right_list = [i for i in tail if i > pivot]   

    # 재귀
    return quick_sort(left_list) + [pivot] + quick_sort(right_list)

print(quick_sort(array))

###########################################################################


array1 = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
def quick_sort1(array, start, end):
    # 원소가 하나인 경우 종료
    if start >= end:
        return # None
    
    # 인덱스
    pivot = start # 피벗
    left = start + 1 # 피벗을 제외
    right = end # array 끝 인덱스 

    # 마지막 인덱스 값 까지 확인
    # left = 큰 데이터, right = 작은 데이터
    while left <= right:

        # 왼쪽, 오른쪽 동시에 확인
        # 왼쪽에서부터 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1 # 1씩 증가시키며 하나씩 확인

        # 오른쪽에서부터 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1 # 오른쪽에서부터 하나씩 반대로 확인(= 인덱스)

        # 엇갈렸다면 작은 데이터와 피벗을 교체
        # = 왼쪽에서부터 찾는 값과 오른쪽에서부터 찾는 값의 위치가 서로 엇갈린 경우
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]

        else:
            array[left], array[right] = array[right], array[left]

    # left가 더 크면 while 종료
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort1(array, start, right-1) # right - 1 ==> 피벗 제외
    quick_sort1(array, right + 1, end) # right + 1 ==> 피벗 제외

# len(array1) - 1 => 인덱스 접근을 위함
quick_sort1(array1, 0, len(array1) - 1)
print(array1)
