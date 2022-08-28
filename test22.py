import sys

input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

start = 0
end = max(tree)

# 나무 최대 높이까지의 절단기
res = 0
while(start <= end):

    total = 0
    mid = (start+end) // 2

    # 시작점부터 끝점까지 각 절단기 길이마다의 합
    # 나무가 중간값보다 컸을때만 자를 수 있음
    for i in tree:
        if i > mid:
            total += i - mid

    if total < m:
        end = mid - 1

    else:
        res = mid
        start = mid + 1
        
print(res)