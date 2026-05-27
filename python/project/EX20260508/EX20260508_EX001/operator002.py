# --------------------- 조건문

'''

if 조건문: True 인 경우 실행문을 실행 ,False 인 경우 실행문을 실행하지 않음
(빈칸4)실행문

 if키워드   조건식   콜론(필수임)
   if      num > 10   :
   
'''

'''

if키워드 : 조건문을 선언하기 위한 키워드로 '만약 ~라면' 의 뜻을 지님
조건식   : 특정 조건을 기술한다. 조건식의 결과에 따라 실행문의 실행 여부가 결정됨
실행문   : 조건식의 결과가 'True' 인 경우 실행함, 'False'의 경우 실행하지 않음        
콜론( : ): 코드블록의 시작을 나타내는 것으로 콜론 이후부터가 실행될 문장
코드블록 : 실행문이 시작되고 끝나는 부분 {테스트}   테스트가 코드블록이됨
들여쓰기 : if 조건문 밑에 빈칸(0칸만 아니면 괜찮음) 뜻함  
           # 실행문의 들여쓰기는 통일해야함
           # "1번 실행문"이 4칸인데 "2번 실행문"이 5칸이면 실행안됨
pass     : 조건문이하 실행문을 입력할수 없는 경우 "pass" 를입력하면 해당 조건문을 건너뜀
           건너뛰기에 에러는 발생하지 않음

'''
   
# num = 5                             # num 은 5다
# if num > 10:                        # num이 10보다 크면 다음을 실행해라
#     print('num은 10보다 크다.')     # num 이 10보다 작기에 실행을 하지않음(결과값 자체가 없음)
#     print('num은 10보다 크다.')     # num 이 10보다 작기에 실행을 하지않음(결과값 자체가 없음)
# print('num은 10보다 크다.')     # 들여 쓰기가 없기에 해당 내용은 실행문 코드블록이 아님
                                  # if 조건문에 관계없이 실행이 됨


# 사용자가 입력한 정수가 10보다 크면 실행문을 출력하는 프로그램
# num = int(input('정수를 입력하세요'))
# if num > 10:
#     print(f'{num}은 10보다 크다.')

# if num == 10:
#     print(f'{num}은 10이랑 같다.')

# if num < 10:
#     print(f'{num}은 10보다 작다.')

#Quiz 속도위반 경고
# 제한속도가 50km/h 인 도로에서 속도위반을 확인하여 단속된차량에게 경고하는 프로그램

# speed = int(input('자동차의 속도를 입력하세요'))
# if speed > 50:
#     print(f'당신의 현재 속도는 {speed}km/h 입니다 감속하세요.')

'''
if ~ else : 만약 ~ 라면 그러나 else(그렇지않다면) , 양자택일 의 경우만 쓸수있음  1번 아니면 2번
'''

# 예제문-----------------
# myScore = 90
# if myScore >= 90:
#     print('용돈 겟')

# if myScore < 90:
#     print('빠따 겟')

# 위 명령과 아래 명령은 동일함

# myScore = 80
# if myScore >= 90:
#     print('용돈 겟')
# else:
#     print('빠따 겟')  

'''
if ~ elif : 다중 선택
'''
# ---------------예제문
# 점수가 90이상이면    A 학점
# 점수가 80이상 90미만 B 학점
# 점수가 70이상 80미만 C 학점
# 점수가 60이상 70미만 D 학점
# 점수가 50이상 60미만 E 학점
# 점수가 50미만이면    F 학점

# Score = int(input('점수를 입력하세요'))
# if Score >= 90:
#     print('A')

# if 80 <= Score < 90:
#     print('B')

# if 70 <= Score < 80:
#     print('C')

# if 60 <= Score < 70:
#     print('D')

# if 50 <= Score < 60:
#     print('E')

# if 50 > Score:
#     print('F')
#---------------------------------------------------------------
# Score = int(input('점수를 입력하세요'))
# if Score >= 90:
#     print('A')

# elif 80 <= Score:
#     print('B')

# elif 70 <= Score:
#     print('C')

# elif 60 <= Score:
#     print('D')

# elif 50 <= Score:
#     print('E')

# elif 50 > Score:
#     print('F')


# Quiz 자동 주문 시스템 만들기
'''
다국어를 지원하느 식당에서 사용할 자동 주문 시스템을 만들경우
1번을 누르면 한국어로 표기 
2번을 누르면 영어로 표기
3번을 누르면 중국어로 표기
4번을 누르면 영어로 표기
하여 주문을 받는 프로그램
'''
# 1.한국어 2. English 3. 中國語
# 1. 주문하시겠습니까?
# 2. Would you like to order?
# 3. 您要点菜吗？
# 4. Would you like to order?





# choice = int((input('언어를 선택하세요.')))

#1 = 주문하시겠습니까?'
#2 = Would you like to order?'
#3 = 您要点菜吗?'
#4 = Would you like to order?'
# if choice == 1:
#     print('주문하시겠습니까?')
# if choice == 2:
#     print('Would you like to order?')
# if choice == 3:
#     print('您要点菜吗?')
# if choice == 4:
#     print('Would you like to order?')

# KOREAN = 1
# ENGLISH = 2
# CHINESE = 3

# if choice == KOREAN:
#     print('주문하시겠습니까?')
# elif choice == ENGLISH:
#     print('Would you like to order?')
# elif choice == CHINESE:
#     print('您要点菜吗?')
# else:
#     print('Would you like to order?')
    
'''
#Quiz) 국가 재난 지원금 수령액 조회하기
표를 참고하여 프로그램 생성
1인가구 : 400,000  원
2인가구 : 600,000  원
3인가구 : 800,000  원
4인이상 : 1,000,000원
'''

# houseHold = int(input('가구원 수를 입력하시요.'))

# if houseHold == 1:
#     print(f'지원 금액은 400,000원 입니다.')
# elif houseHold == 2:
#     print(f'지원 금액은 600,000원 입니다.')
# elif houseHold == 3:
#     print(f'지원 금액은 800,000원 입니다.')
# else:
#     print(f'지원 금액은 1,000,000원 입니다.')


'''
리팩토링(refactoring): 프로그램의 동작은 그대로 유지하며, 코드의
                       구조를 더 깔끔하고 효율적으로 바꾸는 작업.

핵심 포인트
기능은 바꾸지 않음 → 결과는 동일해야함.
코드 품질 개선 → 가독성, 유지보수성, 확장성을 높임.
중복 제거, 의미 있는 이름 사용, 구조 단순화 등이 대표적인 리팩토링 기법.
'''

# houseHold = int(input('가구원 수를 입력하시요.'))

# ONEPERSON = 1
# TWOPEOPLES = 2
# THREEPEOPLES = 3

# if houseHold == ONEPERSON:
#     print(f'지원 금액은 400,000원 입니다.')
# elif houseHold == TWOPEOPLES:
#     print(f'지원 금액은 600,000원 입니다.')
# elif houseHold == THREEPEOPLES:
#     print(f'지원 금액은 800,000원 입니다.')
# else:
#     print(f'지원 금액은 1,000,000원 입니다.')


'''
다음 요구사항을 충족하는 프로그램을 만드시오
 - BMI 지수를 입력한다.
 - BMI 지수가 90 이하면 '저 체중'을 출력한다.
 - BMI 지수가 90 초과 ~ 110 이하면 '정상 체중'을 출력한다.
 - BMI 지수가 110 초과 ~ 120 이하면 '과 체중'을 출력한다.
 - BMI 지수가 120 초과 ~ 140 이하면 '비만'을 출력한다.
 - BMI 지수가 140 초과면 '고도 비만'을 출력한다.

'''

# Bmi = int(input('Bmi지수를 입력하세요.'))

# if Bmi  <= 90:
#     print(f'저 체중')
# elif Bmi <=110:
#     print(f'정상 체중')
# elif Bmi <= 120:
#     print(f'과 체중')
# elif Bmi <= 140:
#     print(f'비만')
# else:
#     print(f'고도 비만')


# 중첩 조건문
# 조건문 내에 또 다른 조건문을 쓸 수 있는데, 이를 중첩 조건문이라고 합니다.
# 사용자가 입력한 정수에서 양수(0을제외)인지를 판단하여 양수라면 홀인지 짝인지 구분하기

# myInterger = int(input('정수를 입력하세요.'))
# if myInterger > 0:                       # myInterger 가 0보다 큰 수인지 판단을함
#     if myInterger % 2 == 0:              # myInterger 를 2로 나누엇을때 나머지가 0 과 일치한지를 판단을 함 0과 일치한다면 짝수 일치하지않는다면 홇수
#         print('짝수')
#     else:
#         print('홀수')
# else:
#     print('음수')        



# 홀짝 판별기 프로그램
# num = int(input('양의 정수를 입력하세요.'))
# if num > 0:
#     if num % 2 == 0:
#         print('짝수')
#     else:
#         print('홀수')
# else:
#     print('입력한 정수는 0, 음수입니다.')


# Quiz)
'''
출생연도 끝자리와 나이를 입력하면 다음 요구사항에 맞춰 마스크 구매 가능한 요일을 출력하는 프로그램
 - 공적 마스크 판매 관련하여 출생연도 끝자리르 이용한 5부제를 다음과 같이 실시함.
 - 1,6 → 월
 - 2,7 → 화
 - 3,8 → 수
 - 4,9 → 목
 - 5,0 → 금
 - 만 65세이상은 요일에 관계없이 구매 가능
'''



# endBirth = int(input('출생년도 끝자리를 입력 하세요'))
# age = int(input('나이를 입력하세요'))
# if age < 65:
#     if endBirth == 1 or endBirth == 6:
#         print('월요일에 구매가 가능하십니다.')
#     elif endBirth == 2 or endBirth == 7:
#         print('화요일에 구매가 가능하십니다.')
#     elif endBirth == 3 or endBirth == 8:
#         print('수요일에 구매가 가능하십니다.')
#     elif endBirth == 4 or endBirth == 9:
#         print('목요일에 구매가 가능하십니다.')
#     elif endBirth == 5 or endBirth == 0:
#         print('금요일에 구매가 가능하십니다.')

# else:
#     print(f'요일에 관계없이 언제든 구매 가능하십니다.')



# 날짜 관련 모듈 : datetime
# 1번째 데잇타임은 큰범주 2번쨰는 그중에서 날짜와 시간만

# 현재 일(day) 구하기
# print(datetime.today().weekday()) # 4가 출력됨( 0=월, 1=화 2=수, 3=목 ...)
# from datetime import datetime
# print(datetime.today().day)

# Quiz
'''
차량 2부제 프로그램 
차량번호 4자리를 입력하여 홀수인지 짝수인지구분
홀수날은 홀수차량 입차가능
짝수날은 짝수차량 입차가능
'''


# from datetime import datetime

# dayNumber = (datetime.today().day)
# carNumber = int(input('차량번호 4자리를 입력하세요.'))
    
# print(f'오늘날짜: {dayNumber} 일입니다.')

# if dayNumber % 2 ==0:
#     print('오늘 입차: 번호가 짝수인 차량')
# else:
#     print('오늘 입차: 번호가 홀수인 차량')

# if dayNumber % 2 == carNumber % 2:
#     print('귀하의 차량은 금일 입차가 가능한 차량입니다.')
# else:
#     print('귀하의 차량은 금일 입차가  불가능한 차량입니다.')


# Quiz)
'''
심정지 환자에게 AED를 최초로 사용했을때 시간에 비례하여 환자의 생존율을 나타낸것
장비를 사용하기에 걸린시간을 입력하면 생존율을 나타내는 프로그램
'''

# time = int(input('AED를 사용하기 까지 걸린 시간(초)을 입력하세요.'))

# if time <= 60:
#     print('생존율: 85%')
# elif time <= 120:
#     print('생존율: 76%')
# elif time <= 180:
#     print('생존율: 66%')
# elif time <= 240:
#     print('생존율: 57%')
# elif time <= 300:
#     print('생존율: 47%')
# else:
#     print('생존율: 25% 미만')



# Quiz)
'''
전기를 많이 사용하면 누진세가 붙어 단가와 기본요금이 올라간다.
누진세가 적용된 단가표를 참고하여 전기사용량을 입력하면 전기료가 출력되는 프로그램

            200kwh 이하 사용시 단가 99.3  기본요금 910
200kwh 초과 400kwh 이하 사용시 단가 187.9 기본요금 1600
            400kwh 초과 사용시 단가 280.6 기본요금 7300

전기료 방식 기본요금 + (사용량*단가)

       예시 910원 + (190kwh * 99.3) = 910원 +(18867) = 19777
'''
# elecEnergy = int(input('전기 사용량을 입력하세요'))

# if elecEnergy <= 200:
#     elecBill = (elecEnergy * 99.3 + 910)
#     print(f'당월 전기사용량은{elecEnergy}kwh 이므로, 전기료는{elecBill}원 입니다')
# elif elecEnergy <= 400:
#     elecBill = (elecEnergy * 187.9 + 1600)
#     print(f'당월 전기사용량은{elecEnergy}kwh 이므로, 전기료는{elecBill}원 입니다')
# elif elecEnergy > 400:
#     elecBill = (elecEnergy * 280.6 + 7300)
#     print(f'당월 전기사용량은{elecEnergy}kwh 이므로, 전기료는{elecBill}원 입니다')



# Quiz) 신장을 입력하면 놀이기구 탑승 여부가 출력되는 프로그램 120이상 160이하 만 탑승이 가능
# height = int(input('신장을 입력하세요'))

# if 120 <= height <= 160:
#     print('가능') 
# else:
#     print('불가능') 



# import random    # 난수 발생 모듈

# ranNum = random.randint(1, 3)          # 1 부터 3까지 정수중 하나발생함
# myNum = int(input('1. 가위, 2.바위, 3. 보입력하세요'))

# if ranNum == 1 and myNum ==1:
#     print('Draw')
# elif ranNum == 1 and myNum ==2:
#     print('Player: Win, COM: Lose')
# elif ranNum == 1 and myNum ==3:
#     print('Player: Lose, COM: Win')

# elif ranNum == 2 and myNum ==1:
#     print('Player: Lose, COM: Win')
# elif ranNum == 2 and myNum ==2:
#     print('Draw')
# elif ranNum == 2 and myNum ==3:
#     print('Player: Win, COM: Lose')

# elif ranNum == 3 and myNum ==1:
#     print('Player: Win, COM: Lose')
# elif ranNum == 3 and myNum ==2:
#     print('Player: Lose, COM: Win')
# elif ranNum == 3 and myNum ==3:
#     print('Draw')
# -----------------------------리팩토링------------------------------

# import random    # 난수 발생 모듈

# ranNum = random.randint(1, 3)          # 1 부터 3까지 정수중 하나발생함
# myNum = int(input('1. 가위, 2.바위, 3. 보입력하세요'))

# if (ranNum == 1 and myNum ==1) or (ranNum == 2 and myNum ==2) or (ranNum == 3 and myNum ==3):
#     print('Draw')
# elif ranNum == 1 and myNum ==2 or (ranNum == 2 and myNum ==3) or (ranNum == 3 and myNum ==1):
#     print('Player: Win, COM: Lose')
# elif ranNum == 1 and myNum ==3 or (ranNum == 2 and myNum ==1) or (ranNum == 3 and myNum ==2):
#     print('Player: Lose, COM: Win')



# Quiz) 
'''
사용자가 입력한 문자 메시지 길이에따라 SMS 또는 MMS의 발송을 결정하느 프로그램
문자 메세지의 길이가 50 이하면 SMS로 발송, 그렇지 않다면 MMS로 발송
'''

# str = 'hello'
# print(f'str: {str}')                # hello
# print(f'str length: {len(str)}')     # 5      len은 메시지의 글자수를 세어줌       \는 점시 기능을 멈춤 앞에쓰임



# useMsg = input('메시지를 입력하세요.')
# msgLen = len(useMsg)

# if msgLen <= 50:
#     print('SMS 발송')
# else:
#     print('MMS 발송')
