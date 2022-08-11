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

n = 25
k = 5
cnt = 0

while True:
    if n % k == 0:
        cnt +=1
        n = n // k
    
    elif n == 1:
        break
print(cnt)

array = [[0]*5 for _ in range(5)]

array[0][1] = [1,1]

print(array)

x = ["a", "b", "c", "d", "e", "f", "g", "h"]

for i in x:
    print(ord(i))

# s = [list(map(int, input().split())) for _ in range(3)]
# print(s)

s = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]
print(s[1][1])