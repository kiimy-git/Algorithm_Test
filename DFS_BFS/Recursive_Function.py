def recursive_func():
    print("재귀 함수 호출")

    # 함수 재 호출
    recursive_func()

recursive_func()
'''
RecursionError: maximum recursion depth exceeded while calling a Python object  
- 재귀 함수 호출 문자열을 무한히 호출하게 됨
- 정의한 함수가 자기 자신을 계속해서 추가로 불러오기 때문
- 어느 정도 출력하다가 해당 에러가 발생함
=> 재귀(recursion)의 최대 깊이를 초과했다는 내용
'''