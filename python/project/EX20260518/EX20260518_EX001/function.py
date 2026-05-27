'''
함수란 : 특정 기능을 정의한 구문으로 기능을 재 사용하기 위해 사용함.
VS 변수: 데이터를 관리하기 위한 메모리 공간으로 데이터를 재 사용하기위해 사용함
'''

# 함수 생성시 기능을 많이넣지말걸 
# 함수는 기능을 재 사용하기 위함
# 변수는 데이터를 재 사용하기 위함

'''
 함수명 규칙
 내장 함수명과 동일하면 안됨
 첫 글자는 소 문자로시작
 첫 글자는 숫자 표기 불가
 특수 문자는 안되나, 언더바(_) 는 가능
 2개 이상의 단어가 조합되는 경우 카멜표기법
'''

'''
--- 함수 기본 문법 구조 ---
def 함수이름():
    기능(실행문)


예시) 인삿말이 출력되는 함수
def printIntro():         # printIntro 라는 함수를 만듦(함수 선언)
    print('안녕')         # 함수를 출력하면 '안녕'이 출력됨(실행문)

printIntro()              # 함수를 출력(함수호출) | 출력하면 함수의 실행문인 '안녕'이 출력됨    
'''
# # 함수 선언부
# def startTemperatureSensor():
#     print('온도센서 작동을 시작합니다.')
    
# def stopTemperatureSensor():
#     print('온도센서 작동을시중지합니다.')

# # 함수 호출
# startTemperatureSensor()
# stopTemperatureSensor()


# Quiz 내 노트북은 몇 인치일까?
'''
노트북 구매했는데 노트북 사이즈에 맞는 파이치를 구매하려한다 사이즈 표에 인치로만 표기되어있음
cm 을 인치로 바꿔주는 함수를 만들어라
1 inch = 2.54cm
1 cm = 0.3937 inch
'''

# lengthCm = float(input('길이(cm)를 입력하세요.'))
# print(f'인치변환: {lengthCm * 0.3937}inch')

# def convertUnit():
#     lengthCm = float(input('길이(cm)를 입력하세요.'))
#     print(f'{lengthCm * 0.3937}inch')

# convertUnit()


# QUiz) 이동 거리를 계산하는 함수
'''
길동이는 5시간 동안 3km의 속도로 등산을했습니다.
길도이가 이동한 시간과 속도를 입력하면 이동한 거리를 계산해 주는 프로그램
'''

# time = float(input(f'이동한 시간(단위: Hour)'))
# speed = float(input(f'이동 속도(단위: Km/h)'))

# #distance = (time) * (speed)

# def calculateDistance():
#     print (f'이동거리는 {(time) * (speed)}km입니다.')

# calculateDistance()

# # 함수 내에서 또 다른 함수를 호출
# def fun1():
#     print('fun1() called')
# def fun2():
#     print('fun2() called')

# def fun3():    
#     fun1()
#     fun2()
#     print('fun3() called')    
        
# fun3()


# # 재기 함수
# # 무한루프에 빠지게됨 그러나 오류로 멈춤

# def fun4():
#     print('fun4() called')
#     fun4()

# fun4()


# Quiz) 다국어 인사말 프로그램
'''
출신 국가를 선택하면 해당하는 국가의 인사말이 출력되는 프로그램
1. 대한민국   2. USA   3. JAPAN
'''

# def introKor():
#     print('한국어임')

# def introEng():
#     print('영어임')

# def introJap():
#     print('일본어임')

# selectedMenuNum = int(input('Where are you from?   1. 대한민국   2. USA   3. JAPAN'))

# if selectedMenuNum == 1:
#     introKor()

# elif selectedMenuNum == 2:
#     introEng()

# elif selectedMenuNum == 3:
#     introJap()


# Quiz) 계산기 프로그램
'''
사용자가 숫자 2개를 입력하고 연산자를 선택하면 연산결과가 출력되는 프로그램
''' 

def calculator():

    if selectedOperator == 1 :  # 덧셈
        add()

    elif selectedOperator == 2 :    # 뺼셈
        sub()

    elif selectedOperator == 3 :    # 곱셈
        mul()

    elif selectedOperator == 4 :    # 나눗셈
        dib()


inputNum1 = float(input('숫자를 입력하세요')) 
selectedOperator = int(input('연산자 선택:    1. 덧셈   2. 뺄셈   3. 곱셈   4. 나눗셈'))
inputNum2 = float(input('숫자를 입력하세요'))


def add():
    print(f'덧셈 결과는 {inputNum1 + inputNum2}')

def sub():    
    print(f'뺄셈 결과는 {inputNum1 - inputNum2}')

def mul():
    print(f'곱셈 결과는 {inputNum1 * inputNum2}')

def dib():  
    print(f'나눗셈 결과는 {inputNum1 / inputNum2}')

calculator()


# 지역변수와 전역변수가있음


num = 1 # 전역변수
        # 전역변수는 함수 내에서도 사용이 가능하다 변수값이 수정되면 오류가발생함


def nums():
    num = 1   # 지역 변수
              # 지역 변수는 전역에서쓸수없음, 함수 내에서만 적용이됨


# global 키워드
# 함수 내부에서 전역변수를 수정하고싶을떄 사용을함




