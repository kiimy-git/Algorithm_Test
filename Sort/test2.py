# 성적이 낮은 순서로 학생 출력하기
'''
2
홍길동 95
이순신 77
'''

import sys

input = sys.stdin.readline

n = int(input())

student = [input().split() for _ in range(n)]

array = []
for i in student:
    i[1] = int(i[1])
    array.append(i)

for i in sorted(array, key= lambda x : x[1]):
    print(i[0], end=' ')

########################################################################

n = int(input())

array1 = []

# 한번에 바꿔줌
for i in range(n):
    input_data = input().split()

    array1.append((input_data[0], int(input_data[1])))

array1 = sorted(array1, key= lambda student : student[1])

for i in array1:
    print(i[0], end= ' ')