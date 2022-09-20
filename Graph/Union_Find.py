## 각각 루트 노드를 찾아서 더 큰 루트 노드가 더 작은 루트 노드를 가리키도록 구현

'''
가장 먼저 노드의 개수(V) 크기의 부모 테이블을 초기화한다. 이때 모든 원소가 자기 자신을
부모로 가지도록 설정한다. 현재 원소의 개수가 6이므로, 초기 단계에서는 총 6개의 트리가 존재

<유의할점>
부모 테이블은 말 그대로 부모에 대한 정보만을 담고 있다. 다시말해 특정한 노드의 부모에 대해서만 저장
실제로 루트를 확인하고자 할 때는 재귀적으로 부모를 거슬러 올라가서 최종적인 루트 노드를 찾아야 한다.
6 4
1 4
2 3
2 4
5 6

# 사이클
3 3
1 2
1 3
2 3
'''

import sys

input = sys.stdin.readline

v, e = map(int, input().split())

# 부모 테이블 초기화
# + 1을 해주는 이유는 노드 번호가 첫 번째로 시작하기 때문에 이후 출력시 이해하기 쉽게 하기위함
parent = [0] * (v + 1)

# 특정 원소가 속한 집합 찾기 / 같은 루트 노드를 가지는 것이 있을 경우 한 번 더 확인
def find_parent(parent, x):

    # 루트 노드가 아니라면, 루트 노드를 찾을때까지 재귀
    if parent[x] != x:
        return find_parent(parent, parent[x])
    
    return x

## 경로 압축 Path Compression
'''
위와 같은 find함수의 경우는 비효율적으로 동작
<예시>
(4, 5), (3, 4), (2, 3), (1, 2)와 같이 주어졌을 때 노드 5의 루트를 찾기 위해서는
노드 5 -> 노드 4 -> 노드 3-> 노드 2-> 노드 1 순서대로 부모 노드를 거슬러 올라가야하므로 최대 O(V) 시간 소요
노드의 개수가 V, find(), union() 연산의 개수가 M개일 때, 전체 시간 복잡도 O(VM)
= So, 부모 테이블값을 갱신함으로써 루트 노드에 더 빠르게 접근할 수 있다.
'''
def find_parent_com(parent, x):

    if parent[x] != x:

        # 부모 테이블 값 갱신
        parent[x] = find_parent(parent, parent[x])

    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent_com(parent, a)
    b = find_parent_com(parent, b)

    if a < b:
        parent[b] = a

    else:
        parent[a] = b

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 사이클 여부
cycle = False

for i in range(e):
    a, b = map(int, input().split())
    
    # 사이클 발생 조건
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    
    # 사이클 발생하지 않는다면 union연산 수행
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
for i in range(1, v+1):
    print(find_parent_com(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
for i in range(1, v+1):
    print(parent[i], end=" ")

## 사이클 여부
if cycle:
    print("사이클 발생")

else:
    print("사이클 발생 X")