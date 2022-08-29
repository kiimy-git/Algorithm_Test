import sys
'''
input = sys.stdin.readline

m = list(map(int, input().split()))

print(m)
'''

a = [1, 2, 3, 4, 5]
b = [2, 3, 4, 5, 6]

res = list(map(lambda a, b: a+b, a, b))

print(res)

lista = []
for i in range(8):
    lista.append(i)

print(lista)

n = 25
k = 5
cnt = 0

while True:
    if n % k == 0:
        cnt +=1
        n = n // k
    
    elif n == 1:
        break
print(cnt)

array = [[0]*5 for _ in range(5)]

array[0][1] = [1,1]

print(array)

x = ["a", "b", "c", "d", "e", "f", "g", "h"]

for i in x:
    print(ord(i))

# s = [list(map(int, input().split())) for _ in range(3)]
# print(s)

s = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]
print(s)

d = 0
direction = [0, 1, 2, 3]

def turn_left(direct):
    global d
    # 북 서 남 동
    # 0 3 2 1
    if direction[direct] == d:
        if d == 0:
            d = direction[-1] # 3

        d = direction[direction[direct] - 1]
    
    return d

from collections import deque

data = deque([2,3,4])
data.appendleft(1)
data.append(5)
data.popleft()
data.reverse()
print(list(data))

# 뭔 차이지???
print(1.1 + 0.1 == 1.2)
print(0.3 + 0.6 == 0.9)
print(0.5 + 0.4 == 0.9)
print(0.6 + .6 == 1.2)

print(3 // 2)

import numpy as np
ss = np.array([[False, True, True, False], [True, True, True, False], [False, True, True, True], [False, False, True, False]])

n, m = map(int, input().split())

# 현재 위치에서 바라보고 있는 방향
x, y, direction = map(int, input().split())

# 육지, 바다
size_map = [list(map(int, input().split())) for _ in range(n)]

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화 = True, False
d = [[0] * m for _ in range(n)]
d[x][y] = 1 # 현재 위치 방문 처리

# 이동(= 북 동 남 서)
dx = [-1, 0, 1, 0]
dy = [0, 1 , 0, -1]

def turn_left1():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
print(turn_left1())
while True:
    # 방향 전환 = 처음 방향에 육지가 있을 수 있는데 먼저 확인해야하지 않나???
    turn_left1()

    # 왜 에러가 나지??? TypeError, list하고 int는 더해지지 않는다..
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and size_map[nx][ny] == 0:
        d[nx][ny] = 1
        x, y = dx, dy
        count += 1
        turn_time = 0

    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if size_map[nx][ny] == 0:
            x, y = nx, ny

        else:
            break
        turn_time = 0

print(count)



def binary_search(array, target, start, end):
    if start > end:
        return None

    # mid 설정
    mid = (start + end) // 2

    # 조건
    # 중간값과 타겟값이 같을때
    if array[mid] == target:
        return mid
        
    # 중간값이 크면 끝점 이동
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)

    # 중간값이 작으면 시작점 이동
    else: # array[mid] < target:
        return binary_search(array, target, mid+1, end)


