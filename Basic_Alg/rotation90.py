# 2020년 카카오 자물쇠와 열쇠 문제

import numpy as np

def rotation_90(a):
    row_length = len(a)
    column_length = len(a[0])

    # 초기화 행렬 생성(90도 회전했을 때 형태)
    res = [[0]*row_length for _ in range(column_length)]
    print(np.array(res))

    for r in range(row_length): # 0 1 2
        for c in range(column_length): # 0 1 2 3
            res[c][row_length-1-r] = a[r][c]
    print(np.array(res))
    return res

a = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
print(rotation_90(a))