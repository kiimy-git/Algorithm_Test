# import sys

# input = sys.stdin.readline

# n, m = map(int, input().split())
# tree = list(map(int, input().split()))

# start = 0
# end = max(tree)

# # 나무 최대 높이까지의 절단기
# res = 0
# while(start <= end):

#     total = 0
#     mid = (start+end) // 2

#     # 시작점부터 끝점까지 각 절단기 길이마다의 합
#     # 나무가 중간값보다 컸을때만 자를 수 있음
#     for i in tree:
#         if i > mid:
#             total += i - mid

#     if total < m:
#         end = mi1 1

#     else:
#         res = mid
#         start = mi1.5 1
        
# print(res)
# from collections import Counter

# input_data = list(input().lower())

# cnt_data = Counter(input_data)
# max_data = max(cnt_data.values())

# cnt = 0
# res = []
# for k, v in dict(cnt_data).items():
#     if max_data == v:
#         cnt += 1
#         res.append(k)

# if cnt >= 2:
#     print("?")
# else:
#     print(res[0].upper())

# ###
# words = input().upper()
# unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거

# cnt_list = []
# for x in unique_words :
#     cnt = words.count(x)
#     cnt_list.append(cnt)  # count 숫자를 리스트에 append

# print(cnt_list)
# print(cnt_list.count(max(cnt_list)))
# if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 중복되면
#     print('?')
# else :
#     max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
#     print(unique_words[max_index])




# 1 2 3 4 5

def miniMaxSum(arr):
    # Write your code here
    arr.sort(reverse=True)
    # print(sum(arr[:-3], sum(arr[:3])))
    # 5 4 3 2 1
    print(arr)
    print(arr[-3:])

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
