# 상하좌우
# 1. 내가 푼 방법
'''
5
R R R U D D
'''

import sys

input = sys.stdin.readline

n = int(input())

input_move = input().split()

# ["L", "R", "U", "D"]
# move = [[-1, 0], [1, 0], [0, -1], [0, 1]]

x = 1
y = 1

# 1보다 작으면 무시
# n보다 크면 무시
for i in input_move:
    if i == "L":
        if x-1 == 0:
            continue
        x -= 1
    
    if i == "R":
        if x+1 > n:
            continue
        x += 1

    if i == "U":
        if y-1 == 0:
            continue
        y -= 1

    if i == "D":
        if y+1 > n:
            continue
        y += 1

print(y, x)

############################################################

n = int(input())
x, y = 1, 1
input_move = input().split()

# L, R, U, D
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ["L", "R", "U", "D"]

for plan in input_move:
    for i in range(len(move_types)):
        # 인덱스로 접근
        if plan == move_types[i]:
            # 값을 계속 갱신
            # 새로운 변수로 할당 하는 이유
            # - 공간 벗어날 때의 조건 적용이 안됨
            nx = x + dx[i]
            ny = y + dy[i]

    # 공간을 벗어나는 경우
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    # 스와핑
    x, y = nx, ny

print(x, y)

