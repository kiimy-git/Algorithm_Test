import sys
import math

input = sys.stdin.readline

m, n = list(map(int, input().split()))

# 소수 == True
prime_data = [True for i in range(1000001)]
prime_data[1] = 0 # 1은 소수가 아님

# 나열한 수 중에서 아직 처리하지 않은 가장 작은 수를 찾는다(입력 값)
for i in range(2, int(math.sqrt(n) + 1)): # n의 제곱근(가운데 약수)까지만 증가시킴
    if prime_data[i] == True: # or prime_data[i]:
        j = 2
        # i = 2, 3, 4
        # n = 16
        while i * j <= n: # 가장 작은 수를 제외한 배수를 제거
            prime_data[i*j] = False # 
            j += 1 # 배수 증가

for i in range(m, n+1):
    if prime_data[i]:
        print(i, end=" ")

print(prime_data[:2])