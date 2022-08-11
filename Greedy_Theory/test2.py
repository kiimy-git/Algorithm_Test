# 숫자 카드 게임
# 1. 내가 푼 방법
import sys

input = sys.stdin.readline

# m = 열, n = 행
n, m = map(int, input().split())
res = []

for i in range(n):
    array = list(map(int, input().split()))
    min_val = min(array)
    res.append(min_val)

print(max(res))

#######################################################

import sys

input = sys.stdin.readline

# m = 열, n = 행
n, m = map(int, input().split())
result = 0

for i in range(n):
    array = list(map(int, input().split()))
    min_val = min(array)

    result = max(result, min_val)

print(result)