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

from collections import defaultdict
people = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]

report_dict = defaultdict(set)
# for i in people:
#     report_dict[i] = []

result_dict = defaultdict(set)

for i in range(len(report)):
    p1, p2 = report[i].split()
    report_dict[p1].add(p2)

    # result_dict[p2] = set()
    result_dict[p2].add(p1)
print(report_dict)
print(result_dict)

score = [0 for _ in range(len(people))]

for i in range(len(people)):
    user = people[i]

    if user not in report_dict.keys():
        continue

    for bad in report_dict[user]:
        if len(result_dict[bad]) >= 2:
            score[i] += 1

print(score)


# result [2, 1, 1, 0]