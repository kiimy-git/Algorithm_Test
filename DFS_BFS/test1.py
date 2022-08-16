# 음료수 얼려 먹기
# 얼음 틀의 모양이 주어졌을 때, 생성되는 총 아이스크림 개수

# 각 위치에서 상하좌우의 위치는 인접한 노드인 것처럼 가정을 하고
# n*m 그래프 상황에서 DFS, BFS를 사용할 수 있음

'''
## output을 어떤 조건으로 가져올지 먼저 고려
1. 방향에 따른 이동 체크 함수
2. 해당 함수 map(n*m)에 적용

4 5                  
00110
00011
11111
00000

15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
'''

import sys
# 재귀 제한 
# python에서는 재귀의 한도가 시스템의 안정을 위해 정해져있음
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

# 세로, 가로
n, m = map(int, input().split())

# 얼음틀
# readline으로 가져올 경우 \n이 같이 나옴
size_map = [list(map(int, input().strip())) for _ in range(n)]

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 2. 이동 경로 체크
def dfs(x,y):
    # 현재 위치 방문 처리 (0,0) 부터
    size_map[x][y] = 1
    
    # 네 방향을 다 보고 나면 return 으로 None이 나옴
    for i in range(4):
        
        nx = x + dx[i]
        ny = y + dy[i]

        # 틀 안에 있을 때
        if 0 <= nx < n and 0 <= ny < m:
            
            # 다음 위치가 0이였을 때 재귀함수 적용
            if size_map[nx][ny] == 0:                
                dfs(nx, ny)

    # return None

# 아이스크림 개수
cnt = 0

# 1. 전체를 다 봐야한다.
for i in range(n):
    for j in range(m):          
        # 처음 (0,0) 위치부터 시작      
        if size_map[i][j] == 0:
            dfs(i,j)
            cnt += 1

print(cnt)

########################################################################
print()

# 세로, 가로
n, m = map(int, input().split())

# 얼음틀
# readline으로 가져올 경우 \n이 같이 나옴
graph = [list(map(int, input().strip())) for _ in range(n)]

def dfs1(x, y):
    # 얼음틀 밖에 있을 경우
    # if x <= -1 and x >= n and y <=-1 and y >= m:
    #     return False

    # 얼음틀 안에 있을 때만 고려
    if 0 <= x < n and 0 <= y < m:

        if graph[x][y] == 0:
            graph[x][y] = 1 # 방문 처리

            # 상 하 좌 우 재귀호출
            # == return 값을 사용하지 않기 때문에 단순히 연결된 모든 노드에 대해서 
            # 방문처리를 수행하기 위한 목적으로 수행됨
            dfs1(x-1, y)
            dfs1(x, y-1)
            dfs1(x+1, y)
            dfs1(x, y+1)
            return True

    return False

count = 0
for i in range(n):
    for j in range(m):
        # 시작점 노드가 방문처리가 되었다면 즉, 처음 방문한 것이라면
        if dfs1(i,j) == True:
            count += 1
print(count)