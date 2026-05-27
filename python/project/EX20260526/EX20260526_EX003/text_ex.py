# 파일을 다루는 것 은 3단계로 이루어짐

# 1 파일 열기
'''
파일을 열기 위해서는 open() 함수를 사용함
성공하면 파일은 객체로 만들어져 메모리에 생성됨
'''

# 2 파일 읽기, 쓰기
'''
문자열을 쓰거나 읽는 단계
문자열을 쓸때는 write()함수를 사용, 읽을때는 read()라는 함수를 이용
'''

# 3 파일 닫기
'''
쓰기, 읽기가 끝난 파일은 닫을때, close()라는 함수를 이용
'''


# file = open('C:/ktk/KTK/python/test.txt', 'w') # open(파일경로, 목적) w = write
# result  = file.write('hello python')           # 쓰기(write)
# print(f'result: {result}')                     # 반환 값은 12 | 12의 의미는 쓰여진 문자열의 길이를 의미함.
# file.close()                                   # 닫기(외부 자원 해제)


# file = open('C:/ktk/KTK/python/test.txt', 'r')   # open(파일경로, 목적) r = read 
# readResult = file.read()                         # 쓰기(write)
# print(f'readResult: {readResult}')               # 현재 텍스트파일은 123
# print(f'readResult type: {type(readResult)}')    # str  읽어오는 데이터는 문자열이다.  

# readResult = int(readResult)                     # readResult 를 정수형으로 변환
# readResult += 1                                  # 정수형으로 변환한 readResult에 1을 더하여 재할당

# print(f'readResult: {readResult}')               # 124 가 출력
# file.close()                                     # 닫기(외부 자원 해제)


# file = open('C:/ktk/KTK/python/test.txt', 'w')     # open(파일경로, 목적) w = write
# file.write('hello')                                # hello를 입력하고
# file.close()                                       # 파일을 닫는다

# file = open('C:/ktk/KTK/python/test.txt', 'w')     # write 를 쓰면 전에 저장한내용은 사라짐
# file.write('Hi')                                   # 새로 입력한 hi만 남게됨
# file.close()                                       # 파일을 닫음

# # ---------------------------------------------------------------------------------------------------------

# file = open('C:/ktk/KTK/python/test.txt', 'w')     # write 를 쓰면 전에 저장한내용은 사라짐
# file.write('hello')                                # hello를 입력하고
# file.close()                                       # 파일을 닫는다

# file = open('C:/ktk/KTK/python/test.txt', 'a')     # a 는 파일뒤에 내용을 추가함. append 와 동일함.
# file.write('\nHi')                                 # 새로 입력한 hi만 남게됨
# file.close()                                       # 파일을 닫음


# ------------------------------------------------------------------------------------------------------------

# with open('C:/ktk/KTK/python/test.txt', 'a') as file:       # with open(파일경로, 목적) as file: file = open(경로, 목적) 과 동일함 close()구문도 함꼐해줌 
#     file.write('\n hello~')                                 # 작성이 끝낫기에 close()를 쓰지않아도 됨.

# ------------------------------------------------------------------------------------------------------------

# 예외 처리(보험)
'''
세상에 모든 프로그램은 내부적인 요인이든, 외부적인 요인이든, 100% 완벽할수가 없음.
'''

# print(10 + 20)      # 30  출력
# print(10 / 0)       # 에러 발생
# print(10 - 20)      # 실행 안함
# print(10 * 20)      # 실행 안함

# 예외 처리의 기본 문법
'''
try ~ except 문법을 사용함

'''
# print(10 + 20)     
# try:                # 실행을 하나
#     print(10 / 0)  
# except:             # 문제가 발생하면 실행문을 진행
#     pass            # 넘김
# print(10 - 20)     
# print(10 * 20)     



# print(10 + 20)     
# try:                               # 실행을 하나
#     print(10 / 0)  
# except Exception as e:             # 문제가 발생하면 실행문을 진행
#     print(f'e: {e}')               # 에러 내용을 출력하고 넘김 | e: division by zero
# print(10 - 20)     
# print(10 * 20)     
# -------------------------------------------------------------------
 
# try:                               # 실행을 하나
#     print(10 + 20)                 # 정상 출력
#     print(10 / 0)                  # 에러 발생해서 e에 할당 후 종료해버림
#     print(10 - 20)                 # 실행 하지 않음
#     print(10 * 20)                 # 실행 하지 않음
# except Exception as e:             # 문제가 발생하면 실행문을 진행
#     print(f'e: {e}')               # 에러 내용을 출력하고 넘김

# try except 는 에러가 발생할 것 같은 문구에만 사용할 것


# print(10 + 20)     
# try:                                         # 실행을 하나
#     print(10 / 10)                           # 0과 10으로 실행해보면됨
# except Exception as e:                       # 문제가 발생하면 실행문을 진행
#     print(f'e: {e}')                         # 에러 내용을 출력하고 넘김 | e: division by zero
# else:
#     print('에러가 발생하지 않으면 실행되는 코드')    
# finally:
#     print('에러 발생 유무 상관없이 무조건 실행되는 코드')    
# print(10 - 20)     
# print(10 * 20)     









































