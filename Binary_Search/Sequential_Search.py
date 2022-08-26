# 순차 탐색
'''
리스트 내에서 특정한 데이터를  찾기 위해 앞에서부터 데이터를 
하나씩 매우 빠르게 탐색하는 이진 탐색 알고리즘

# input
# 생성할 원소 개수와 찾고자 하는 문자열
5 apple
banana orange apple melon watermelon 

# output
# 문자열 위치(몇 번째에 있는지)
3
'''

import sys

input = sys.stdin.readline

n, s = input().split()
array = list(input().split()) # list 안해줘도 되네??? = map()사용시만

cnt = 1
for i in range(int(n)):

    if s == array[i]:
        # 따로 cnt를 선언하지 않고
        # 반복문 돌린 i + 1을 return 해주면 됨
        # print(i+1)
        break
    
    cnt += 1

print(cnt)


#####################################################################

# 구현
def sequential_search(n, target, array):
    
    for i in range(n):

        if array[i] == target:
            return i + 1

input_data = input().split()
n = int(input_data[0])
target = input_data[1]

array = input().split()
print(array)
print(sequential_search(n, target, array))