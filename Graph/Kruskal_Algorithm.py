"""
1. 간선 데이터를 비용에 따라 오름차순으로 정렬(= 가장 거리가 짧은 간선부터 차례대로)
2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
    - 사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킨다.
    - 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다.
3. 모든 간선에 대하여 2번의 과정을 반복

노드 개수, 간선 개수
첫번째 노드와 두번째 노드를 연결했을 때 거리
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
"""

## 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):

    # 루트 노드가 아니라면, 루트 노드를 찾을때까지 재귀
    if parent[x] != x:

        # 부모 테이블 값 갱신
        parent[x] = find_parent(parent, parent[x])

    return parent[x]

## 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a

    else:
        parent[a] = b

import sys

input = sys.stdin.readline

v, e = map(int, input().split())
parent = [0] * (v+1) # 부모 테이블 초기화

## 최종 비용을 담을 변수
res = 0

## 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

## 그래프의 모든 간선 정보만 따로 빼내어 정렬 수행
info = [list(map(int, input().split())) for i in range(e)]

## 전체 간선 데이터를 리스트에 담은 뒤에 정렬
sort_info = sorted(info, key= lambda x : x[2])
'''
edges = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
'''

## 가장 짧은 간선이 선택되고 union 함수 수행
for edge in sort_info:
    a, b, cost = edge
    print(a, b, cost)
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        res += cost

print(parent)
print(res)