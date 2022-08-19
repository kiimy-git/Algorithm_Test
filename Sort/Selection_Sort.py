from random import randint
import time

# 선택 정렬(selection Sort)
array = []

for _ in range(1000):
    array.append(randint(1, 100))

print(array)

starttime = time.time()
# 인덱스 접근
for i in range(len(array)):

    # 가장 작은 데이터 선택
    min_index = i

    # 다음 값과 비교
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
            
    # 스와핑
    array[i], array[min_index] = array[min_index], array[i]
endtime = time.time()
print(f"시간{endtime - starttime}\n", array)

# array 초기화 / 기본 정렬(Sort) 라이브러리
array = []
for _ in range(1000):
    array.append(randint(1, 100))

start_time = time.time()

array.sort()
end_time = time.time()

print(f"시간{end_time - start_time}\n", array)