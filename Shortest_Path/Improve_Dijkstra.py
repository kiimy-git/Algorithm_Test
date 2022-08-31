# 방법 2
## 기본 원리는 동일
## 1차원 리스트(최단 거리 테이블)는 그대로 이용
## 현재 가장 가까운 노드를 저장하기 위한 목적으로만 우선순위 큐를 추가로 이용

## get_smallest_node()를 작성할 필요가 없음
# = 최단 거리가 가장 짧은 노드를 선택하는 과정을 다익스트라 최단 경로 함수 안에서
# 우선순위 큐를 이용하는 방식으로 대체할 수 있기 때문

import sys
import heapq

# 입력되는 데이터의 수가 많다는 가정하에 해당 방법 적용
input = sys.stdin.readline

# 대부분 문제에서는 그래프의 간선 길이 정보를 줄 때 1억 미만값으로 준다.
INF = int(1e9) # 무한을 의미하는 값으로 10억 설정

n,m = map(int, input().split())

# 시작 노드 
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n+1)]

# 방문 여부
visited = [False] * (n+1)

# 최단 거리 테이블 모두 무한으로 초기화
d = [INF] * (n+1)

# 모든 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())

    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

def dijkstra(start):

    # 우선순위 큐 넣을 리스트
    q = []

    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 튜플 큐에 삽입
    heapq.heappush(q, (0, start))
    d[start] = 0

    while q: # q가 비어있지 않다면

        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시:
        if d[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]

            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < d[i[0]]:
                d[i[0]] = cost

                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
print(d)
for i in range(1, n+1):

    # 도달할 수 없는 경우
    if d[i] == INF:
        print("무한")

    # 시작노드에서 부터 도달할 수 있는 경우의 거리를 모두 출력
    else:
        print(d[i])