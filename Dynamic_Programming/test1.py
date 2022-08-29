# 1로 만들기
'''
Greedy Test3하고 차이가 있음(= 나누눈 작업이 더 값을 빠르게 줄일수 있기 때문에)
So, 해당 문제는 큰 수로 나눈 것이 더 값을 줄일 수 있어보이지만 다른 연산을 적절히 섞어서
더 빠르게 줄일 수 있기 때문에 단순히 그리디 해법으로는 어렵다
'''
# 1. x가 5로 나누어떨어지면, 5로 나눈다
# 2. x가 3으로 나누어떨어지면, 3으로 나눈다
# 3. x가 2으로 나누어떨어지면, 2으로 나눈다
# 4. x에서 1을 뺀다
# x를 1로 만들때, 연산을 사용하는 횟수의 최솟값을 출력

'''
26 - 1 = 25 (4)
25 / 5 = 5 (1)
5 / 5 = 1 (1)
'''

import sys

input = sys.stdin.readline

x = int(input())

# 26 - 25 - 5 - 1

cnt = 0
while True:

    if x % 5 == 0:
        x /= 5
        cnt += 1

    elif x % 3 == 0:
        x /= 3
        cnt += 1

    elif x % 2 == 0:
        x /= 2
        cnt += 1

    elif x == 1:
        break

    else:
        x -= 1
        cnt += 1
    
## 틀림
print(cnt)
# 26 - 13 - 12 - 4 - 2 - 1

##############################################################
import time
# !!호출되는 과정을 그림으로 그려보기!!
'''
                        26
                13              25
        12                  5       24       
     4   6  11          1        8  12  23        
'''
# 다이나믹 프로그래밍(= 메모이제이션 바텀업)
x = int(input())

# DP 테이블 초기화
# 한 번 계산된 결과 "메모이제이션"
# index = " 금액 " / value = " 방법 "
m = [0] * 30001
start = time.time()
# m[0]은 없다고 치고, m[1] = 0 이므로 m[2]부터 쌓아나간다.
for i in range(2, x+1):

    # 네 가지 경우 
    # 현재의 수에서 1을 빼는 경우
    m[i] = m[i-1] + 1 # +1 == count

    if i % 2 == 0:
        m[i] = min(m[i], m[i // 2] + 1)

    elif i % 3 == 0:
        m[i] = min(m[i], m[i // 3] + 1)

    elif i % 5 == 0:
        m[i] = min(m[i], m[i // 5] + 1)
end = time.time()
print(m[x], end - start)

###############################################################

# 재귀 함수 사용(= 딕셔너리 이용)
# 더 빠르긴 하지만 조건 하나 추가시 재귀 에러남
x =int(input())

memo = {1: 0, 2: 1}
start = time.time()
def dp(n):
    if n in memo:
        return memo[n]
	
    # 핵심 코드 + dp(n//5) + n%5 == RecursionError: maximum recursion depth exceeded
    cnt = 1 + min(dp(n//3) + n%3, dp(n//2) + n%2)
    memo[n] = cnt
    print(memo)
    return cnt
end = time.time()
print(dp(x), end - start)
'''
{1: 0, 2: 1, 4: 2}
{1: 0, 2: 1, 4: 2, 8: 3}
{1: 0, 2: 1, 4: 2, 8: 3, 3: 1}
{1: 0, 2: 1, 4: 2, 8: 3, 3: 1, 6: 2}
{1: 0, 2: 1, 4: 2, 8: 3, 3: 1, 6: 2, 13: 4}
{1: 0, 2: 1, 4: 2, 8: 3, 3: 1, 6: 2, 13: 4, 26: 5}
'''