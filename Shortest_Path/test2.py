# 전보
'''
N개의 도시가 있고, 각 도시는 보내고자 하는 메시지가 있는 경우, 다른 도시로 전보를
보내서 다른 도시로 해당 메시지를 전송할 수 있다. 하지만 X라는 도시에서 Y라는 도시로
전보를 보내고자 한다면, 도시 X에서 Y로 향하는 통로가 설치되어야 한다.
예를 들어 X에서 Y로 향하는 통로는 있지만, Y에서 X로 향하는 통로가 없다면 Y는 X로
메시지를 보낼 수 없다.

메시지는 도시 C에서 출발하여 각 도시 사이에 설치된 통로를 거쳐, 최대한 많이 퍼져나갈 것이다.
각 도시의 번호와 통로가 설치되어 있는 정보가 주어졌을 때, 도시 C에서 보낸 메시지를 받게
되는 도시의 개수는 총 몇 개이며 도시들이 모두 메시지를 받는 데까지 걸리는 시간은???
- 특정 지역을 거쳐서 가는 내용이 아님 == 다익스트라 문제

(도시 개수), (통로의 개수), (메시지를 보내고자 하는 도시C)
(둘째 줄부터 m+1번째 줄에 걸쳐서 통로에 대한 정보 x, y, z가 주어짐)
특정 도시 x에서 다른 특정 도시 y로 이어지는 통로가 있으며, 시간
3 2 1
1 2 4
1 3 2

2 4
'''

import sys
import numpy as np
import heapq

input = sys.stdin.readline

n, m, c = map(int, input().split())

INF = int(1e9)

graph = [[] for _ in range(n+1)]

d = [INF] * (n+1)

for i in range(m):
    x, y, z = map(int, input().split())

    # Y에서 X로 향하는 통로가 없다면 Y는 X로 메시지를 보낼 수 없다.
    graph[x].append((y,z))

print(graph)

def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    d[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if d[now] < dist:
            continue

        for i in graph[now]:
            # i[1] == i 노드에서의 거리 값
            cost = dist + i[1]

            # i[0] == 노드, 
            if cost < d[i[0]]:
                d[i[0]] = cost

                # 값이 갱신될 때마다 기록될 수 있게
                heapq.heappush(q, (cost, i[0]))

# 메시지는 도시 C에서 출발
dijkstra(c)

# 메시지를 받게 되는 도시의 개수 
# 도시들이 모두 메시지를 받는 데까지 걸리는 시간
cnt = 0
max_d = 0
for res in d:
    if res != INF:
        cnt += 1
        max_d = max(max_d, res)

# 시작 노드는 제외
print(cnt -1, max_d)