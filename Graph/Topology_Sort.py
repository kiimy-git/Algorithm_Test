"""
1. 진입차수가 0인 노드를 큐에 넣는다
2. 큐가 빌 때까지 다음의 과정을 반복
    - 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거
    - 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
    
    = 이때 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재한다고 판단할 수 있다.
    다시 말해 큐에서 원소가 V번 추출되기 전에 큐가 비어버리면 사이클이 발생 
    사이클이 존재하는 경우 사이클에 포함되어 있는 원소 중에서 어떠한 원소도 큐에 들어가지 못하기 때문
    다만, 보통 기본적으로 위상 정렬 문제에서는 사이클이 발생하지 않는다고 명시하는 경우가 더 많음

7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
"""

import sys
from collections import deque

input = sys.stdin.readline

v, e = map(int, input().split())

## 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)

## 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 A에서 B로 이동 가능
    indegree[b] += 1 # 진입차수 1 증가


## 위상 정렬 함수
def topology_sort():
    res = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() 

    ## 처음 진입차수가 0인 노드(= i)를 큐에 넣는다
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    ## 큐가 빌 때까지 반복
    while q:
        now = q.popleft()
        res.append(now)

        ## 처음 진입 차수가 0인 노드와 연결되어 있는 간선 제거 
        ## = 해당 노드와 연결된 노드 진입차수 -1 
        for i in graph[now]:
            indegree[i] -= 1

            ## 새롭게 갱신된 진입차수가 0인 노드를 큐에 삽입 
            if indegree[i] == 0:
                q.append(i)

    for i in res:
        print(i, end=" ")

topology_sort()
