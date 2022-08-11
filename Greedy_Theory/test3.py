# 1이 될 때까지
# 1. 내가 푼 방법
import sys
import time

input = sys.stdin.readline

n, k = map(int, input().split())

# 최소 횟수
cnt = 0

start = time.time()
while True:
    if n % k == 0:
        n //= k
        cnt += 1

    elif n == 1:
        break

    else:
        n -= 1
        cnt += 1

end = time.time()
print(cnt)
print(end - start)

#######################################################

input = sys.stdin.readline

n, k = map(int, input().split())

count = 0

# n이 k보다 크면 계속 나누기
while n >= k:
    while n % k != 0: # 나누어지지 않으면(= 조건문이 아니라 반복문??)
        n -= 1
        count += 1

    # 나누고 나머지 값 갱신
    n //= k
    count += 1

# n이 k 보다 작으면 -1, count
while n > 1:
    n -= 1
    count += 1

print(count)

#######################################################

input = sys.stdin.readline

n, k = map(int, input().split())

result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break

    result += 1
    n //= k

result += (n-1)
print(result)