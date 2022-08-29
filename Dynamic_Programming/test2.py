# 개미 전사
# 선택적으로 약탈하여 식량을 빼앗을 예정
# 서로 인접한 식량창고가 공격받으면 바로 알아챌 수 있다
## 식량창고 n개에 대한 정보가 주어졌을 때 얻을 수 있는 식량의 최댓값
'''
4
1 3 1 5

6 
1 4 2 4 4 5
'''
import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

# 빼앗은 식량, DP 테이블 초기화
m = [0]* 1001

# 해당 숫자를 선택했을때 다음 숫자는 무조건 (n + 2)
for i in range(n):
    next_num = i + 2

    if next_num >= n:
        continue
    m[i] = array[i] + array[next_num]


## 틀림
print(m[n-3])

########################################################################

n = int(input())
array = list(map(int, input().split()))

# 한 번 계산된 결과 "메모이제이션"
# index = " 금액 " / value = " 방법 "
d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])

# 왼쪽부터 차례대로 식량창고를 털지 안 털지를 결정하는 경우와 특정한 i번째 식량창고에
# 대해서 털지 안 털지의 여부를 결정할 때
for i in range(2, n):
    # 1. (i-1)번째 창고를 털기로 결정한 경우 현재의 식량창고를 털 수 없다
    # 2. (i-2)번째 창고를 털기로 결정한 경우 현재의 식량창고를 털 수 있다
    # 따라서, 1과 2번 중 더 많은 식량을 털 수 있는 경우를 선택하면 된다
    # d[i-3]은 고려하지 않아도되 == d[i-1]과 d[i-2]을 구하는 과정에서 이미 계산되었기 때문
    d[i] = max(d[i-1], d[i-2] + array[i])

# 반복문 2~3, d(i = 3)
print(d[n-1])



