# Bottom Up 방식에서 사용되는 결과 저장용 리스트를 DP 테이블라고 부름
# DP테이블 초기화
m = [0] * 100

m[1] = 1
m[2] = 1
n = 99

# Bottom Up 다아니막 프로그래밍 
for i in range(3, n+1):
    m[i] = m[i - 1] + m[i - 2]

print(m[n])