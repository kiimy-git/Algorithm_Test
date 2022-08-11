# 왕실의 나이트

# 수평 2칸, 수직 1칸
# 수직 2칸, 수평 1칸

import sys

alp, n = list(sys.stdin.readline().strip())

dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]

loc_x = ["a", "b", "c", "d", "e", "f", "g", "h"]
size = len(loc_x)

cnt = 0

for i in range(size):
    for v in range(size):
        if loc_x[i] == alp:
            nx = i+1 + dx[v]
            ny = int(n) + dy[v]

            if nx > size or ny > size or nx < 1 or ny < 1:
                continue
            cnt += 1
print(cnt)

#################################################################

# ord(문자) = 유니코드 정수
# chr(정수) = 유니코드 문자
# 유니코드와 아스키코드의 차이???
'''
아스키코드 = 1바이트 == 8 비트만으로 표현된 방식(2의 8제곱 = 256)
* 아스키코드에서 마지막 1비트는 parity bit으로 통신상의 에러나 변조 가능성의 검출을 위해 사용
* 그래서 아스키코드는 128개 문자를 표현

유니코드 = 2바이트 == 16 비트로 표현(2의 16 제곱 = 65536개 만큼 문자 표현가능)
'''

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [
    (-2, -1), (-1, -2), (1, -2), (2, -1), 
    (2, 1), (1, 2), (-1, 2), (-2, 1)
]

res = 0
for step in steps:
    nx = row + step[0]
    ny = column + step[1]

    if nx >=1 and nx <=8 and ny >=1 and ny <=8:
        res += 1

print(res)
