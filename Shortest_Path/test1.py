# 미래 도시
'''
A는 현재 1번 회사에 위치해 있으며, X번 회사에 방문해 물건을 판매하고자 한다
특정 회사에 도착하기 위한 방법은 회사끼리 연결되어 있는 도로를 이용하는 방법이 유일
또한 연결된 2개의 회사는 양방향으로 이동할 수 있다.
특정 회사와 도로로 연결되어 있다면, 정확히 1만큼의 시간으로 이동할 수 있다

A는 X번 회사에 가서 물건을 판매하기 전에 다른 회사를 방문할 예정
따라서 1번 회사에서 출발하여 K번 회사를 방문한 뒤에 X번 회사로 가는 것이 목표
A는 가능한 빠르게 이동하고자 한다
A와 회사 사이를 이동하게 되는 최소 시간을 계산하는 프로그램을 작성
만약 도달할 수 없는 곳이면 -1 출력
= 특정 지역을 거쳐서 갈 경우 == 플로이드 워셜

(회사 개수n), (경로 개수m)
(둘째 줄부터 m +1번째 줄에는 연결된 두 회사의 번호가 공백으로)
(m+2, 마지막줄에는 X와 K가 공백으로 구분되어 차례대로 주어짐)
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

4 2
1 3
2 4
3 4
'''

import sys
import numpy as np

input = sys.stdin.readline

n, m = map(int, input().split())

# 무한
INF = int(1e9)

# 노드 graph
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용 0으로 초기화
# 정사각형이였을때만 가능
for i in range(1, n+1):
    graph[i][i] = 0

print(np.array(graph))

# 간선 개수
for i in range(m):
    a, b = map(int, input().split())

    # 특정 회사와 도로로 연결되어 있다면, 정확히 1만큼의 시간으로 이동할 수 있다
    graph[a][b] = 1
    ## 다시 돌아오는 길도 
    graph[b][a] = 1

print(np.array(graph))

# K번 회사를 방문한 뒤에 X번 회사로
x, k = map(int, input().split())

# A는 현재 1번 회사에 위치 = 1번부터 시작, 갱신
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

print(np.array(graph))

d = graph[1][k] + graph[k][x]

if d >= INF:
    print(-1)
else:
    print(d)