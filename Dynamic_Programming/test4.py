# 효율적인 화폐 구성

'''
인덱스(금액) = [0, 1, 2, 3, 4, 5 ....]
a[0] = 0

화폐 단위 2 부터 확인 
a[2] => 화폐 2원 = 1가지 / a[2] = a[0] + 1이 된다 
a[4] => 2원, 2원 = 2가지 / a[4] = a[2] + 1
*a[6] => (2원, 2원, 2원) = 3가지*

화폐 단위 3 
a[3] => 3원 = 1가지
a[5] => 2원, 3원 = 2가지
*a[6] => 3원, 3원 = 2가지*
a[7] => 2원, 2원, 3원 = 3가지

화폐 단위 5
a[5] => 5원 = 1가지
a[7] => 2원, 5원 = 2가지

중복되는 인덱스가 나오고 더 작은 방법 개수(=value)로 갱신해준다.
2 15
2 
3

3 4
3
5
7
'''

import sys

input = sys.stdin.readline

# n가지 종류의 화폐, 개수를 최소한으로 이용해서 그 가치의 합이 M
# 적은 금액부터 큰 금액까지 확인
n, m = map(int, input().split())

m_type = [int(input()) for _ in range(n)]

# m -= m_type
# index = " 금액 " / value = " 방법 "
# 한 번 계산된 결과 "메모이제이션"
d = [10001] * (m + 1)
d[0] = 0

for i in range(n):
    for j in range(m_type[i], m+1):
        # if d[j - m_type[i]] != 0:
        d[j] = min(d[j], d[j - m_type[i]] + 1) 

if d[m] == 10001:
    print(-1)

else:
    print(d[m])

