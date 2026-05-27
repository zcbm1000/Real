# 지역변수 vs 전역변수
# 지역변수는 함수 내부에서 선언된 변수로, 함수 내부에서만 사용이 가능함
# 전역변수는 함수 외부에서 선언된 변수로, 함수 내/외부에서 사용이 가능함

'''
함수에서 전역변수를 참조, 조회는 가능함.
함수에서 전역변수를 수정하려고 하면 오류가 발생을함.
global 이라는 키워드를 이용해 함수내에서 전역변수를 수정이 가능함
'''




# num = 10                       # 전역변수를 선언

# def fun():
#     num = 20                  # 지역변수를 선언 
#     print(f'num: {num}')                  

# fun()                         # 출력을 하면 함수 내에 있는 num 을 출력을함
#                               # num: 20 이 출력이됨 (지역변수가 없을시 전역 변수를 활용함)

# print(f'num: {num}')          # 출력을 하면 전역변수인 10을 출력함.



# num = 10       

# def fun():
#     global num               # global 키워드를 이용하여 함수내에서 전역변수의 값을 수정 하려할때 반드시필요
#     print(f'num: {num}')                  

# fun()                         # 출력을 하면 함수 내에 있는 num 을 출력을함
#                               # num: 20 이 출력이됨 (지역변수가 없을시 전역 변수를 활용함)

# print(f'num: {num}')          # 출력을 하면 전역변수인 10을 출력함.






# Quiz) 웹 사이트 누적 방문 횟수 프로그램
# 웹 사이트의 방문 여부를 입력 받아 웹 사이트의 누적 방문 횟수를 출력

# flag = True
# totalVisit = 0

# def countVisitor():
#     global totalVisit 
#     totalVisit += 1

# while flag:
#     selectedMenuNum = int(input('1. 웹 사이트 방문           2. 종료'))
#     if selectedMenuNum == 1:
#         countVisitor()
#         print(f'누적 방문 횟수: {totalVisit}')
#     else:
#         flag = False
#         print('goodbye')



# 매개 변수 (중요도 높음)
# 매개: 둘 사이에서 양편의 '관계를 맺어줌'
# 함수를 사용하기 위해 먼저 함수를 정의하고 필요할 때 호출
# 이 떄 함수를 정의하는 쪽을 함수 정의부(선언부), 함수를 호출하는 쪽을 함수 호출부 라고함.
# 할수를 호출할 때 데이터를 넘겨줄 수 있는데 이 데이터를 '인수'라고 합니다.
# 함수 정의부는 인수를 받으면 '매개변수'라는 변수에 저장을함. 매개변수는 지역변수의 일종.


'''
def greet():
    print(f'홍길동님 안녕하세요')


greet()                             # 홍길동만 프린트가됨

#----------------------------------------------------

def greet(name):                    # name 이라는 매개변수 생성
    print(f'{name}님 안녕하세요')   


greet('홍길동')                     # '홍길동' name에 할당
greet('박세리')                     # '박세리' name에 할당
greet('박찬호')                     # '박찬호' name에 할당

#----------------------------------------------------

def greet(name, age):               # name, age 이라는 매개변수 생성
    print(f'{name}님 의 나이는 {age}입니다.')   


greet('홍길동', 25)                    # '홍길동' name에 할당, 25를 age에 할당
greet('박세리', 25)                    # '박세리' name에 할당, 25를 age에 할당 
greet('박찬호', 25)                    # '박찬호' name에 할당, 25를 age에 할당 
'''

# Quiz) 날씨 기온 습도 강수확률을 입력하면 출력해주는 프로그램

# def forecastWeather(temp, humi, rain):
#     print(f'금일 최고기온은 {temp}도 이며, 습도는 {humi}퍼 입니다. 또한 강수확률은 {rain}퍼 입니다')


# forecastWeather(31, 77, 44)



# Quiz) 학급 학생의 총점과 평균을 구하는 함수
'''
학생의 수는 3명이다.
'''

# def printScoresForStudent(student1, student2, student3):
#     totalScore = student1 + student2 + student3
#     average = totalScore / 3
#     print(f'총합: {totalScore} 점')
#     print(f'평균: {average} 점')

# printScoresForStudent(80, 90, 66)


'''
인수의 갯수를 모르는 경우
'''

# def printScoresForStudent(*scores):         # 인수의 갯수를 모르기에 scores의 타입은 튜플(삭제와 추가할려면 리스트로 변환해야함)
#     totalScore = 0
#     for score in scores:
#         totalScore += score

#     print(f'총합: {totalScore} 점')
#     average = totalScore / len(scores)
#     print(f'평균: {average} 점')   

# printScoresForStudent(80, 90, 66)


# def printScoresForStudent(subject, *scores):         # 인수의 갯수를 모르기에 scores의 타입은 튜플(삭제와 추가할려면 리스트로 변환해야함)
#     totalScore = 0
#     for score in scores:
#         totalScore += score

#     print(f'{subject}총합: {totalScore} 점')
#     average = totalScore / len(scores)
#     print(f'{subject}평균: {average} 점')   

# printScoresForStudent('국어', 80, 90, 66)


# '''
# 선생님이 몇 명일지 모르는 학생의 점수를 입력한다.
# 이때 학생 점수의 총합과 평균을 구하는 함수를 만들고 이를 이용하는 프로그램을 만들어보자!
# '''

# flag = True
# studentScores = []

# def printScoresForStudent(scores):      # scores = [,,,,,,,,,]
#     if len(scores) == 0:
#         print('학생수가 0명이라 총점과 평균을 구할 수 없습니다.')
#     else:
#         totalScore = 0
#         for score in scores:
#             totalScore += score
        
#         average = totalScore / len(scores)   # 0 / 0
#         print(f'총점: {totalScore}')
#         print(f'평점: {average}')
    

# while True:
#     selectedMenuNum = int(input('1.학생 점수 입력     2.종료'))
#     if selectedMenuNum == 1:
#         score = int(input('학생 점수 입력: '))
#         studentScores.append(score)
#     else:
#         # flag = False
#         break

# printScoresForStudent(studentScores)



# # Quiz) 인수의 갯수를 모르는 평균 구하기

# '''
# 몇 명일지 모르는 학생의 점수를 입력
# 학생점수의 총합과 평균을 구하는 함수
# '''
# flag = True
# studentsScores = []

# def printScoresForStudents(scores):
#     totalScore = 0
#     for score in scores:
#         totalScore += score
#     average = totalScore / len(scores)
#     print(f'총점: {totalScore}')
#     print(f'평균: {average}')

# while flag:
#     selectedNum = (int(input('1.학생 점수 입력,     2. 종료')))
#     if selectedNum == 1:
#         score = int(input('학생 점수 입력: '))
#         studentsScores.append(score)
#     else:
#         flag =False    


# printScoresForStudents(studentsScores)




# quiz) SMS와 MMS 구별하기
'''
문자를 보낼 때 100자 이하인 경우에는 단문 메시지(SMS)로 50원을 부과합니다.
100자를 넘어가면 장문 메시지(MMS)로 변경되면서 100원이 부과됩니다. 
단문과 장문을 구별해서 돈을 부과하는 프로그램을 만들어봅시다. 
'''

# inputData = input(f'문자를 입력하세요.')

# def sendUserMessage(str):
#     strLength = len(str)
#     print(f'사용자가 입력한 문자길이: {strLength}')

#     if strLength <= 100:
#         print(f'SMS 발송 완료.')
#         print('50원 부과')
#     else:
#         print(f'MMS 발송 완료.')
#         print('100원 부과')  

# sendUserMessage(inputData)



# 인수와 매개변수의 순서가 일치하지 않을 경우

# def printMemberInfo(name, email, major, grade):   # 이름, 이메일, 전공, 학년
#     print(f'name : {name}')
#     print(f'email: {email}')
#     print(f'major: {major}')
#     print(f'grade: {grade}')

# printMemberInfo('Hong Gildong',
#                  1, 
#                  'Gildong@gmail.com', 
                #  'art')
# 출력을 하면 'name'에 Hong Gildong 'email'에 1
#  'major'에Gildong@gmail.com,m 'grade'에 art 가 위치에 맞지않게 들어감


# def printMemberInfo(name, email, major, grade):
#     print(f'name : {name}')
#     print(f'email: {email}')
#     print(f'major: {major}')
#     print(f'grade: {grade}')

# printMemberInfo(name = 'Hong Gildong',
#                 grade = 1, 
#                 email = 'Gildong@gmail.com',
#                 major = 'art')

# 지정 위치를 주어서 넣을수있음


# def printMemberInfo(info):
#     print(f'name : {info['name']}')
#     print(f'email: {info['email']}')
#     print(f'major: {info['major']}')
#     print(f'grade: {info['grade']}')

# printMemberInfo(
# {   
#     'name': 'Hong Gildong',
#     'grade': 1, 
#     'email': 'Gildong@gmail.com',
#     'major': 'art'
# }
# )



# 매개 변수의 기본값 설정

# 직원 급여 지급 프로그램

# def setSalary(name, pay = 200):     # pay = 200 입력값이 없을경우 기본값이됨
#     print(f'{name}의 급여: {pay}원 지급')

# setSalary('박찬호', 400)   # 출력하면 박찬호의 급여: 400원 지급    
# setSalary('박세리', 600)   # 출력하면 박세리의 급여: 600원 지급   
# setSalary('박용택')        # 출력하면 박용택의 급여: 200원 지금
#                            # 박용택은 pay에 입력한 금액이 없기에 기본값 지급    



# 데이터 반환(return)
# 데이터 반환이란, 함수는 실행이 끝난 후 결과물(값)을 호출부로 반환할수있음
# 이때 사용하는 키워드가 return임.
# 덧셈 연산 함수를 만들어 결과를 출력하는 프로그

# def addFunction(n1, n2):       # 2번 n1 ,n2에 각 10 20을 대입
#     sum = n1+ n2               # 3번 연산하여 30이됨
#     print(f'결과 값: {sum}') 
#     return sum
# result = addFunction(10,20)    # 1번 n1 = 10, n2 = 20 이되니
#                                # 4번 result에 30을 재 할당함

# print(result)                               

#--------------------------------------------------

# def printResult(value):        # 5번 대입하엿으니 실행문 실행
#     print(f'result: {value}')


# def addFunction(n1, n2):       # 2번 n1 ,n2에 각 10 20을 대입
#     sum = n1+ n2               # 3번 연산하여 30이됨
#     print(f'결과 값: {sum}')
#     printResult(sum)           # 4번 sum 을 printResult 매개변수에 대입
#     return sum
# result = addFunction(10,20)    # 1번 n1 = 10, n2 = 20 이되니
#                                # 4번 result에 30을 재 할당함

# print(result)                               


# def fun1():
#     print('111111111')          # 명령을 진행시 11111
#     print('222222222')          #               22222         
#     print('333333333')          #               33333
#                                 # 출력함                 
# fun1()        

# #----------------------------------------------------------

# def fun1():
#     print('111111111')    # 명령을 진행시 11111
#     return                # return 을 하였기에
#     print('222222222')    #               22222
#     print('333333333')    #               33333
#                           # return 밑은 출력하지 않음
# fun1()



# # 별탑 만들기
# def increaseStar(limitStar):
#     print('*')
#     print('**')
#     print('***')
#     print('****')
#     print('*****')
#     print('******')
#     print('*******')
#     print('********')
#     print('*********')
#     print('**********')
#     for n in range(60):
#         print('*'* n)
#         if n== limitStar:
#             break


# increaseStar(4)


'''
처음 프로그램이 실행되면 다음과 같은 메뉴를 출력
메뉴: 1 회원가입   2. 로그인   3. 특정 회원 정보 출력   4. 모든 회원 정보 출력   0. 종료
'1. 회원가입'을 선택하면 회원 ID, PW ,Email, Phone 정보를 입력받아 가입을 진행함.
'2. 로그인'을 선택하면 ID, PW 를 입력바아 로그인 성공, 실패를 출력함
'3. 특정 회원 정보 출력'을 선택하면 회원 ID,PW 를 입력받아 일치하는 회원 정보를 모두 출력
'4. 모든 회원 정보 출력'을 선택하면 가입되어 있는 모든 회원 정보를 출력한다.
'0. 종료'를 선택하면 프로그램을 종료시킨다.
'''





















































































































































































































