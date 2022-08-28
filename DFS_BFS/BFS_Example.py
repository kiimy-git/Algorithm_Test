'''
1. 탐색 시작 노드를 Queue에 삽입하고 방문 처리
2. Queue에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 Queue에 삽입하고 방문처리
3. 2번 과정을 더 이상 수행할 수 없을 때까지 반복
'''

def bfs(graph, start, visited):

    from collections import deque

    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start] = True

    # Queue가 반복될 때 까지
    while queue:

        # Queue에서 가장 먼저 방문한 원소를 뽑는다
        v = queue.popleft()
        print(v, end= ' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [], # 1은 보통 빈 리스트로 시작(= 보통 시작이 1부터) / 첫 번째 노드
  [2, 3, 8], # 첫 번째 노드에서 인접한 노드
  [1, 7], # 두 번째 노드에서 인접한 노드 ... 
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

bfs(graph, 1, visited)