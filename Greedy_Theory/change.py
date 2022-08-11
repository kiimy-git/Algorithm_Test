# 거슬러줘야할 동전의 최소 개수 구하기
# 거스름돈 문제에서 동전의 단위가 서로 배수 형태가 아니라, 무작위로 주어진 경우는 그리디 알고리즘 X

money = [500, 400, 100]
change = 800

cnt = 0
money.sort(reverse=True)
# print(money)

for coin in money:
    cnt += change // coin
    change %= coin

print(cnt)