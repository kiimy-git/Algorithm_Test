'''
* n번째 피보나치 수 = (n-1)번째 피보나치 수 + (n-2)번째 피보나치 수
* 단, 1번째 피보나치 수 = 1, 2번째 피보나치 수 = 1
'''
import time
# 해당 코드 문제 발생
# n이 커질수록 수행 시간이 기하급수적으로 늘어남
# 점화식을 재귀 함수를 사용 == 비효율적
def fibonacci(n):
    if n == 1 or n == 2:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

start = time.time()
print(fibonacci(30))
end = time.time()
print(end - start)