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

import numpy as np
ss = np.array([[False, True, True, False], [True, True, True, False], [False, True, True, True], [False, False, True, False]])

# N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)
