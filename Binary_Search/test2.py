'''
4 6 = 떡의 개수, 떡의 길이
19 14 10 17 = 떡의 개별 높이
만약 절단기 높이를 15 == 4 0 0 2 / 손님은 6cm를 가져간다
output == 요청한 총 길이 m일 때, 적어도 m만큼의 떡을 얻기 위한 절단기 높이 값

떡 높이의 총합은 항상 m 이상
'''

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
h = list(map(int, input().split()))

max_h = max(h)
total = {}

# enumerate 사용해도됨
for i in range(max_h+1):
    le = []
    for j in range(len(h)):
        if i > h[j]:
            le.append(0)
        else:
            le.append(abs(i - h[j]))

    total[i] = sum(le)

print(total)
# 총길이 합이 제일 작은 것의 절단기 높이 출력
res = []
for k, v in total.items():
    if v <= m:
        res.append((k ,v))

print(res[0][0])

################################################################################

# 이진 탐색
# 입력 조건 h의 범위가 굉장히 크기 때문에(10억) 순차 탐색은 시간초과를 받는다
# So, 크기가 크다면 이진 탐색을 먼저 생각해내야함
# 재귀함수로 구현하는 것은 다소 귀찮을 수 있다
# why??? - 현재 얻을 수 있는 떡볶이의 양에 따라서 자를 위치를 결정해야 하기 때문에
 
'''
- 파라메트릭 서치 유형의 문제
파라메트릭 서치란???
- 최적화 문제를 결정문제(= "예", "아니오"로 답하는 문제)로 바꾸어 해결하는 기법 
"원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제"
1. 적절한 높이를 찾을 때까지 절단기의 높이 h를 반복해서 조정하는 것
2. 현재 이 높이로 자르면 조건을 만족할 수 있는가? 를 확인한다.
3. 위의 조건의 만족 여부("예", "아니오")에 따라서 탐색 범위를 좁혀서 해결할 수 있다.
'''

n, m = map(int, input().split())
h = list(map(int, input().split()))

start = 0
end = max(h)

res = 0
while(start <= end):
    total = 0

    # 중간값 설정(= 절단기의 높이)
    mid = (start + end) // 2


    for i in h:
        # 떡의 높이가 절단기보다 높을 때만 자를 수 있음
        # 잘랐을 때의 떡의 양 계산
        if i > mid:
            total += i - mid
    
    # 떡의 양이 부족한 경우 끝점을 감소(떡 길이의 끝)
    # 중간점의 값보다 total(=찾고자하는 값, 필요한 떡의 길이)이 작을 때 
    if m > total:
        end = mid - 1
    
    # 떡의 양이 큰 경우 시작점을 증가(떡 길이의 시작)
    # 중간점의 값보다 total(=찾고자하는 값)이 클 때
    else:
        res = mid # 최대한 덜 잘랐을 때가 정답이므로, res에 기록
        start = mid + 1

print(res)
        


