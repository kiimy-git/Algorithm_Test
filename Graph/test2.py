## 도시 분할 계획

'''
마을은 N개의 집과 그 집들을 연결하는 M개의 길로 이루어져 있다. 길은 어느 방향으로든지 다닐 수 있다.
그리고 길마다 길을 유지하는데 드는 유지비가 든다.
<마을을 2개로 분리할려고 한다.> 각 분리된 마을 안에 있는 임의의 두 집 사이에 경로가 항상 존재해야 한다.
마을에는 집이 하나 이상 있어야 한다.

마을 안에 길이 너무 많다 -> 일단 분리된 두 마을 사이에 있는 길들은 필요가 없으므로 없앨 수 있다.
+ 각 분리된 마을 안에서도 임의의 두 집 사이에 경로가 항상 존재하게 하면서 길을 없앨 수 있다.
위 조건을 만족하도록 길들을 모두 없애고 나머지 길의 유지비의 합을 최소로 하고 싶다.

------------------------------------------------------------------------------------------
전체 그래프에서 2개의 최소 신장 트리를 만들어야 한다 = 마을을 2개로 분리할려고 한다
두 개의 마을로 분할했는데 그 가중치의 합이 최소가 되게 하려면, 처음 그래프에서 가중치가 가장 큰 간선을 끊어주면 된다!
==> 최소 신장 트리를 찾은 뒤에 최소 신장 트리를 구성하는 간선 중에서 가장 비용이 큰 간선을 제거(= 정렬했으니 마지막 cost)
==> 그러면 최소 신장 트리가 2개의 부분 그래프로 나누어짐

7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
'''

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    
    else:
        parent[a] = b

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

parent = [0] * (n+1)

## 부모 테이블 초기화
for i in range(1, n+1):
    parent[i] = i

## 최소 합
res = 0

## 최소 합이니까 우선 cost 비용 오름차순 정렬
info = [list(map(int, input().split())) for i in range(m)]
info_sort = sorted(info, key= lambda x : x[2])

## 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선
last = 0

res_list = []

for edge in info_sort:
    a, b, cost = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        res += cost
        last = cost # 가장 큰 cost == 오름차순 정렬했기 때문에 마지막 cost 값이 나옴
        res_list.append(cost)

print(res)
print(res_list)
