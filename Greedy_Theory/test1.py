# 큰 수의 법칙
# 1. 내가 푼 방법(reverse=True)
data = [6,5,4,4,2]
res = []

while True:
    for i in range(3):
        if len(res) == 8:
            break
        res.append(data[0])
    
    if len(res) == 8:
        break
    res.append(data[1])

print(res)
print(sum(res))

###############################################################

import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())

array = list(map(int, input().split()))
# TypeError: ‘list’ object is not callable
# => 동일 변수가 있으면 에러가 남


# True = 내림차순, default = 오름차순
array.sort()

fir_num = array[n-1]
sec_num = array[n-2]

result = 0

while True:
    for i in range(k):
        # while 반복문 탈출
        if m == 0: 
            break
        result += fir_num
        m -= 1 # 더할 때마다 1을 빼기
    if m == 0:
        break
    result += sec_num
    m -= 1

print(result)

###############################################################

# M의 크가 100억 이상처럼 커진다면 시간 초과 판정받을 수 있음
# 수학적 아이디어 사용(= 반복되는 수열에 대해서 파악)

input = sys.stdin.readline
n, m, k = map(int, input().split())

array = list(map(int, input().split()))

array.sort()

fir_num = array[n-1]
sec_num = array[n-2]

# M = 8, k = 3
# (6 + 6 + 6 + 5) + (6 + 6 + 6 + 5), 일정하게 반복해서 더해지는 특징
# 반복되는 수열의 길이 k+1 

# 따라서, M을 (k+1)로 나눈 몫이 수열이 반복되는 횟수
# 다시 여기에 K를 곱해주면 가장 큰 수가 등장하는 횟수가 된다

# 이때, M이 (K+1)로 나누어 떨어지지 않는 경우도 고려해야한다
# => 나눈 나머지만큼 가장 큰 수가 추가 되므로

# 가장 큰 수가 더해지는 횟수
# int(m / (k+1)) | m // (k+1) = 나눈 몫
cnt = (m // (k+1)) * k 
cnt += m % (k+1) # 나머지 count

final = 0
final += cnt * fir_num # 가장 큰 값들
final += (m-cnt) * sec_num # 총 길이 에서 가장 큰 값 count 빼기
print(final)