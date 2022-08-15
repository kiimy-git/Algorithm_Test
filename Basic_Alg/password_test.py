# 알파벳 정렬
# 6가지

import sys
from itertools import combinations

alpa = ["a", "e", "i", "o", "u"]

'''
input = sys.stdin.readline
l, c = map(int, input().split())
이렇게 사용하니 출력값에 공백이 생김 why???
=> 개행 문자가 입력 끝에 포함돼있음 \n
=> .strip()으로 제거 
'''
input = sys.stdin.readline
l, c = map(int, input().split()) # split default = ' '

# 암호 알파벳 정렬 = 따로 맵핑을 진행하지 않으면 \n 포함돼있음
# => strip 사용
array = input().strip().split()
array.sort()

# 길이가 ㅣ인 조합
for combi in combinations(array, l):
    print("모든 조합: ", combi)
    cnt = 0
    for i in combi:
        if i in alpa:
            cnt += 1

    # 최소 1개의 모음과 최소 2개의 자음이 있는 경우
    if cnt >= 1 and cnt <= l - 2:
        # print(combi)
        print(''.join(combi))