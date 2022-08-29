# 바닥 공사
# (1*2), (2*1), (2*2)
# 2 * n

import sys

input = sys.stdin.readline

n = int(input())

# DP 테이블 초기화
m = [0]* 1001

# 왼쪽부터 차례대로 (i - 1), (i - 2)
# n = 1, (2 * 1) 한 가지
# n = 2, (1 * 2) 2개, (2 * 2) 1개, (2 * 1) 1개 총 3가지
# ==> 덮개를 채우는 방법은 2가지, (2*1) 이미 위에서 해당 경우가 고려되었기 때문

m[1] = 1
m[2] = 3

# 바텀업
for i in range(3, n+1):
    # i-1까지 채워져 있으면 2*1 덮개를 채우는 하나의 경우의 수
    # i-2까지 채워져 있으면 1*2 덮개 2개를 넣는 경우, 2*2 덮개 1개를 넣는 경우 총 2가지의 경우의 수
    # m[i-1] + m[i-2] + m[i-2]
    m[i] = (m[i-1] + (m[i-2] * 2)) % 796796

print(m[n])