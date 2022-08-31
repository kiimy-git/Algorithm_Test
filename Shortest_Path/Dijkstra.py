# 방법 1 다익스트라
## 노드에 대한 정보를 담는 리스트 생성
## 방문 여부
## 최단 거리 테이블 모두 무한으로 초기화
## 순차 탐색 = 값 갱신
'''
(노드개수, 간선의 개수)
(시작노드)
(간선 정보 a, b, c)
6 11 
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

0
2
3
1
2
4
'''
import sys

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

print(graph)
# [[], [(2, 2), (3, 5), (4, 1)], [(3, 3), (4, 2)], [(2, 3), (6, 5)], [(3, 3), (5, 1)], [(3, 1), (6, 2)], []]

# 방문하지 않은 노드이면서 시작 노드와 최단 거리인 노드 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(= index)

    for i in range(1, n+1):
        # 테이블 value 갱신 및 방문하지 않았다면
        if d[i] < min_value and not visited[i]:
            # 갱신
            min_value = d[i]
            index = i

    return index

def dijkstra(start):
    # 시작 노드 초기화
    d[start] = 0
    visited[start] = True

    # 해당 노드 값
    for i in graph[start]:
        # i[0] == node
        # i[1] == 해당 노드와의 거리 값
        d[i[0]] =i[1]

    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
    for j in range(n-1):

        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True

        #현재 노드와 연결된 다른 노드를 확인
        for v in graph[now]:
            cost = d[now] + v[1]

            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < d[v[0]]:

                # 테이블 갱신
                d[v[0]] = cost

dijkstra(start)
print(d)
# [1000000000, 0, 2, 3, 1, 2, 4]

for i in range(1, n+1):

    # 도달할 수 없는 경우
    if d[i] == INF:
        print("무한")

    # 시작노드에서 부터 도달할 수 있는 경우의 거리를 모두 출력
    else:
        print(d[i])