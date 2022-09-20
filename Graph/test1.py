## 팀 결성
'''
"같은 팀 여부 확인" 연산에 대하여 <한 줄에 하나씩> YES or NO로 결과를 출력
"팀 합치기" 연산은 0 a b 형태로 주어진다. 이는 a번 학생이 속한 팀과 b번 학생이 속한 팀을 합친다는 의미
"같은 팀 여부" 연산은 1 a b 형태로 주어진다. 이는 a번 학생과 b번 학생이 같은 팀에서 속해 있는 지를 확인하는 연산

------------------------------------------------------------------------
전형적인 서로소 집합 알고리즘 문제

7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
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

v, e = map(int, input().split())

parent = [0] * (v+1)

## 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i


for i in range(e):
    t, a, b = map(int, input().split())

    if t == 0:
        union_parent(parent, a, b)

    elif t == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")

        else:
            print("NO")