# 미로 탈출
# Implementation test2와 비슷한 문제???
# 탈출하기 위해 움직여야하는 최소 칸의 개수
# BFS - 간선의 비용이 모두 같을 때 최단 거리를 탐색할 때 사용
# 항상 (1,1)에서 출발하므로 그래프 상에서는 (0,0)에서 출발

'''
5 6
101010
111111
000001
111111
111111
'''

import sys
from collections import deque

input = sys.stdin.readline

# 출구
n, m = map(int, input().split())

size_map = [list(map(int, input().strip())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 목적지 n, m을 찾아가야하는데...

# while True:

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if 0 <= nx < len(size_map) and 0 <= ny < len(size_map[0]):
#             if size_map[nx][ny] == 1:
#                 # 값을 갱신
#                 size_map[nx][ny] = size_map[x][y] + 1
#                 # print(size_map)
#                 cnt_list.append((nx,ny))
            
#         if nx == n and ny == m:
#             break
# print(cnt_list)

########################################################################

def bfs(x, y):

    # 현재 위치 queue에 삽입
    queue = deque()
    queue.append((x,y))

    # queue가 비어있으면 종료(= 끝에 도달하면 종료되는것)
    while queue: 
        x,y = queue.popleft()
        # ==> queue에서 0이 삭제되고 x= 0, y= 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(size_map) and 0 <= ny < len(size_map[0]):
                if size_map[nx][ny] == 1:
                    # 값을 갱신
                    size_map[nx][ny] = size_map[x][y] + 1
        
                    queue.append((nx,ny))

    # 가장 오른쪽 아래까지의 최단 거리 반환
    # -1을 하는 이유는??? (n,m) == 출구
    # = size_map은 리스트, 만약 low가 5라면 list에서는 4에 접근해야 마지막 리스트 접근가능
    return size_map[n-1][m-1]

# 항상 (1,1)에서 출발하므로 그래프 상에서는 (0,0)에서 출발
print(bfs(0,0))