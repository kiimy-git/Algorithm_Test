import sys
'''
input = sys.stdin.readline

m = list(map(int, input().split()))

print(m)
'''

a = [1, 2, 3, 4, 5]
b = [2, 3, 4, 5, 6]

res = list(map(lambda a, b: a+b, a, b))

print(res)

lista = []
for i in range(8):
    lista.append(i)

print(lista)