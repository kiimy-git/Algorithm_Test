# Factorial
# DFS의 대표적인 예제 - Stack 자료구조
# 1 * 2 * 3 ....* (n-1) * n

# 1. 반복적으로 구현한 방식
def factorial_normal(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num


# 2 . 재귀적으로 구현한 방식
def factorial_recur(n):
    # 종료 조건
    # 수학적으로 0!, 1!의 값은 1로 같다는 성질을 이용
    # n이 1 이하가 되었을 때 
    if n <= 1: 
        return 1

    # n! = n * (n-1)!을 그대로 코드로 작성
    return n * factorial_recur(n-1)

print(factorial_normal(6))
print(factorial_recur(6))