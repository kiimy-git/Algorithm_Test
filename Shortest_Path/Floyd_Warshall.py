# Floyd-Warshall

## 초기 테이블 설정
# 1. [step 0]에서는 "연결된 간선"은 단순히 그 값을 채워 넣고, 연결되지 않은 간선은 "무한" 이라는 값을 넣는다
# "무한" = int(1e9)
# 2차원 리스트에서 각 값에 해당하는 Dab는 "a에서 b로 가는 최단 거리"

# 2. 자기 자신에서 자기 자신으로 가는 비용은 0이므로, (1 <= i <= n)의 범위를 가지는 모든 i에 대하여 Dii는 0으로 초기화
# 즉, 왼쪽 위에서 오른쪽 아래로 내려가는 대각선에 놓인 모든 원소는 0이다

'''
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2

0 4 8 6
3 0 7 9
5 9 0 4
7 11 2 0
'''

import sys
import numpy as np

input = sys.stdin.readline
INF = int(1e9)

# 노드 개수
n = int(input())

# 간선 개수
m = int(input())

# 무한으로 초기화(= 2차원 리스트, 행렬)
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용 0으로 초기화
# for i in range(1, len(graph)):
#     graph[i][i] = 0

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

print(np.array(graph))


# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화    
for _ in range(m):
    a, b, c = map(int, input().split())

    # A에서 B로 가는 비용은 C
    graph[a][b] = c

# K번의 단계에 대한
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

print(np.array(graph))

for a in range(1, n+1):
    # 해당 코드는 각 노드에 접근할 수 없음
    # for j in range(n):
    #     print(graph[a][1:][j], end= " ")
    # print()
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("무한", end= " ")

        else:
            print(graph[a][b], end= " ")
    print()