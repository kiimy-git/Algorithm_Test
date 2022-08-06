# 순열과 조합
# 순열 - 서로 다른 n개에서 r개를 선택하여 일렬로 나열하는 것
# 보통 경우의 수 값이 아니라 모든 경우(사건)를 다 출력하도록 요구
from itertools import combinations, permutations

data = [1, 2, 3]

for i in permutations(data, 2):
    print(list(i))

print()
for i in combinations(data, 2):
    print(i, end=' ')