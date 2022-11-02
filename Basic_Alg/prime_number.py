'''
소수란??? 
2보다 큰 자연수 중에서 1과 자기 자신을 제외한 자연수로는
나누어떨어지지 않는 자연수
소수는 2보다 큰 자연수에 대하여 정의되므로, 1은 소수에 해당하지 않음
'''

def chk_prime_num(data):
    # 2보다 큰
    for i in range(2, data):
        if data % i == 0:
            return False
    
    return True

'''
개선된 알고리즘
- 하나의 수가 소수인지 판별하는 알고리즘을 O(X)보다 더 빠르게 동작하도록 작성할 수 있음
자연수의 약수가 가지는 특징을 파악하고 있다면 그 원리를 쉽게 이해할 수 있음
- 특징 해당 숫자 제곱근까지만 확인하면 됨 => 소수가 아닌 숫자는 가운데 약수 기준으로 대칭적으로
    2개씩 앞뒤로 묶어서 곱하면 지정한 숫자가 나옴

소수인지 판별해야하는 수가 1,000,000일 때는 반복문 상 2부터 1,000까지만 확인하면 되는 것임
- 시간 복잡도 O(x 1/2제곱) 
'''
import math

def chk_prime_num_plus(data):
    if num == 2:
        return True
    if num == 1 or num % 2 == 0:
        return False
        
    # 2부터 data의 숫자까지 봐야하므로(range(1, 3-1) => range는 1,2까지만 확인함)
    for i in range(2, int(math.sqrt(data)) + 1):
        if data % i == 0:
            return False

    return True

# 에라토스테네스의 체
'''
하나의 수에 대해서 소수인지 아닌지 판별해야 하는 경우가 아니라 수의 범위가 주어졌을 때,
그 전체 수의 범위 안에서 존재하는 모든 소수를 찾아야하는 경우
- 범위 안에 숫자들 중 소수인 것을 찾아야함
- 위의 알고리즘을 이용하는 것은 상당히 느림

1. 2부터 N까지의 모든 자연수 나열
2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾음
3. 남은 수 중에서 i의 배수를 모두 제거(i는 제거하지 않음)
4. 더 이상 반복할 수 없을 때까지 2번과 3번 과정을 반복(while)
'''

n = 26

# 1. 숫자 나열 = 모든 수가 소수(True)인 것으로 초기화 / 0과 1은 제외
array = [True for i in range(n+1)]
array[1] = 0 # 1은 소수가 아님

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i]: 

        j = 2 # i는 제거하지 않음 So, 2부터 시작(배수)
        while i * j <= n:
            array[i*j] = False # i배수 제거
            j += 1

# 2. 2 = 구간 숫자, 2 - 26 사이 소수(= interval)
for i in range(2, n+1):
    if array[i]: # array가 True인것
        print(i, end=" ")

# 몫이 0 이니까 나머지는 그대로
# 나누는 값이 클때 = 나누는 값 기준(=6)으로 나눠야할 값
a = 4
m = 6

print(2 // m)