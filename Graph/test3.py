'''
강의 수
각 강의의 강의 시간과 선수 강의 
N개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 한줄에 하나씩 출력
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1


10
20
14
18
17
'''

## 위상 정렬 Topology Sorting
# 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용할 수 있는 알고리즘
# 매번 간선 정보를 확인하여 결과 테이블을 갱신

import sys
from collections import deque
import copy

input = sys.stdin.readline

n = int(input())

## 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (n+1)

## 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for _ in range((n+1))]

## 각 강의 시간을 0으로 초기화
time = [0] * (n+1)

for i in range(1, n+1):
    data = list(map(int, input().split()))

    # 각 노드 강의 시간
    time[i] = data[0]
    
    ## 선수 강의 개수
    for x in data[1:-1]:
        ## 최종 노드에 들어오는 간선의 개수(= 선수강의 개수)
        indegree[i] += 1

        # 각 노드 간선
        graph[x].append(i)

print(graph,"\n", time,"\n", indegree)
'''
[[], [2, 3, 4], [], [4, 5], [], []] 
[0, 10, 10, 4, 4, 3]
[0, 0, 1, 1, 2, 1]
'''

def topology():
    res = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
    q = deque()

    # 처음 진입차수가 0인 노드(= i)를 큐에 넣는다
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        # 진입차수가 0인 노드를 꺼낸다
        now = q.popleft()
        
        ## now 노드와 연결된 노드(= graph) 
        for i in graph[now]:
            # 인접한 노드에 대하여 현재보다 강의 시간이 더 긴 경우를 찾는다면, 
            # 더 오랜 시간이 걸리는 경우의 시간 값을 저장
            res[i] = max(res[i], res[now] + time[i])

            # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기(= 간선 제거)
            indegree[i] -= 1

            # 간선을 제거 후 진입차수 0을 다시 q에 넣는다
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n+1):
        print(res[i])

topology()
