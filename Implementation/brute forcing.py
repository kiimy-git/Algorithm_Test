# 시각 - 완전탐색 유형(= 가능한 경우의 수를 모두 검사해보는 탐색 방법)
# 경우의 수 

import sys

input = sys.stdin.readline

n = int(input())
h_cnt = 0
m_cnt = 0
s_cnt = 0
# n = 시간

for h in range(n+1):
    if "3" in str(h):
        h_cnt+=1

    for m in range(60):
        if "3" in str(m):
            m_cnt+=1

        for s in range(60):
            if "3" in str(s):
                s_cnt += 1

print(h_cnt)
print(m_cnt)
print(s_cnt)

############################################################
# 따로 보는 것이 아니라 동시에 봐야함

cnt = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if "3" in str(s) + str(m) + str(h):
                cnt += 1

print(cnt)