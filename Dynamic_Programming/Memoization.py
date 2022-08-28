# Memoization
# 한 번 구한 정보를 리스트에 저장
# 다이나믹 프로그래밍을 재귀적으로 수행하다가 같은 정보가 필요할 때는 이미
# 구한 답을 그대로 리스트에서 가져오면 된다.

import time

# 한 번 계산된 결과를 "메모이제이션" 하기 위한 리스트 초기화
m = [0] * 100

def fibo(n):
    # 종료 조건
    print(f"({str(n)})", end= ' ')
    if n == 1 or n == 2:
        return 1    
    
    # 이미 계산했던 것이라면 그대로 반환
    if m[n] != 0:
        return m[n]

    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    m[n] = fibo(n-1) + fibo(n-2)
    return m[n]
    
start = time.time()
print(fibo(99))
end = time.time()
print(end - start)
