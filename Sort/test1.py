# 위에서 아래로 - 내림차순
'''
3
15
27 
12
'''
import sys

input = sys.stdin.readline

n = int(input())

num = [int(input()) for _ in range(3)]

for i in sorted(num, reverse=True):
    print(i, end= ' ')