# 게임 개발
# 각각의 칸은 육지 또는 바다
'''
# 0 육지, 1 바다

1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전)부터 차례대로 갈 곳을 정함

2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면,
    - 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸 전진

3. 왼쪽 방향에 가보지 않은 칸이 없다면,
    - 왼쪽 방향으로 회전만 수행하고 1단계로 돌아감

4. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸의 경우
    - 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
    - 단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춤

# 캐릭터가 방문한 칸의 수를 출력
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''
import sys
import numpy as np

input = sys.stdin.readline

# 세로, 가로 크기
n, m = map(int, input().split())

# 현재 위치에서 바라보고 있는 방향
y, x, d = map(int, input().split())

# 육지, 바다
size_map = [list(map(int, input().split())) for _ in range(n)]

# 0 북, 1 동, 2 남, 3 서
direction = [0, 1, 2, 3]

# 이동
dx = [0, 1, 0, -1]
dy = [-1, 0 , 1, 0]

# 방문 여부 체크
chk = [[False] * m for _ in range(n)]

chk[y][x] = True
size_map[y][x] = 1

# 바라보는 방향, 총 네번 확인
def turn_left(direct):
    global d
    # 북 서 남 동
    # 0 3 2 1
    if d == 0:
        d = direction[-1] # 3

    d = direction[direction[direct] - 1]
    
    return d

# 횟수
cnt = 1 # 처음 지역은 0이기 때문에 1로 시작
dir_cnt = 0 # 방향 전환 횟수

while True:
    nx = x + dx[d]
    ny = y + dy[d]

    # 이동 방향이 가보지 않은 곳이고 육지라면
    if chk[ny][nx] == False and size_map[ny][nx] == 0:
        cnt += 1
        size_map[ny][nx] = 1
        chk[ny][nx] = True
        dir_cnt = 0 # 이동 후 방향 전환 횟수 초기화

        # 스와핑
        x, y = nx, ny 

    chk[ny][nx] = True
    d = turn_left(d) # 방향 전환
    dir_cnt += 1

    if dir_cnt > 4:
        # 방향 유지한 채로 뒤로 한 칸 이동
        nx = x - dx[d]
        ny = y - dy[d]

        if size_map[ny][nx] == 0:
            x, y = nx, ny

        else: # 바다면 break
            break
        dir_cnt = 0

print(np.array(chk))
print(cnt)

##############################################################################

# N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화 = True, False
d = [[0] * m for _ in range(n)]

# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())

d[x][y] = 1 # 현재 좌표 방문 처리 = True

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
    # 방향 전환 = 처음 방향에 육지가 있을 수 있는데 먼저 확인해고 이동해야하지 않나???
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x, y = nx, ny
        count += 1

        # 이동 후 초기화
        turn_time = 0
        # continue = 예외가 있나???

    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x, y = nx, ny
            
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(d)
print(count)