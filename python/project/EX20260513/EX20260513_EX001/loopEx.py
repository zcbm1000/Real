'''
3 6 9 게임 만들기
1부터 99까지의 숫자 중 1씩 증가하며 3, 6, 9 가 들어 있을 때마다 
숫자와 함께 짝!출력
3 짝!
33 짝짝
'''

# for num in range(1,100):

#     firstNum = num // 10
#     seconNum = num % 10
#     clap = ''

# if firstNum == 3 or firstNum == 6 or firstNum == 9:
#     clap += '짝!'
#     print(f'num: {num}, {clap}')

# if seconNum == 3 or seconNum == 6 or seconNum == 9:
#     clap += '짝!'
#     print(f'num: {num}, {clap}')
# if clap


#Quiz) 열차 교차 시간 알아냐기
'''
대전역에는 3개의 노선의 열차가 09시부터 18시까지 교차 운행한다.
3대의 열차가 교차하는 시간을 구해 열차 충돌 사고를 막으세요.
(단 매일 오전 9시 대전역에서 모든 열차가 출발을함.

1노선 | 첫차 09시 | 막차 18시 | 운행 간격 10분 | # 09시 10분, 09시 20분 에 대전역을옴
2노선 | 첫차 09시 | 막차 18시 | 운행 간격 25분 | # 09시 25분, 09시 50분 에 대전역을옴
3노선 | 첫차 09시 | 막차 18시 | 운행 간격 30분 | # 09시 30분, 10시 00분 에 대전역을옴
'''

# trainA = 10
# trainB = 25
# trainC = 30
# A, B      최소 공배수(충돌 하는 간격)
# 50
# B, C      최소 공배수(충돌 하는 간격)
# 150
# A, C      최소 공배수(충돌 하는 간격)
# 30
# A, B, C   최소 공배수(충돌 하는 간격)
# 150

# for n in range(1,541):   # '540'은 기차가 운행하는 총 '시간'을 '분'으로 나타낸것
#                                                                      # trainA trainB 의 교차 
#     if n % trainA == 0 and n % trainB == 0:                          #  10분   25분     교차 = 50분 간격
#         print('A와 B의 충돌시각은')
#         print(9 + n // 60, end='')       #  9시 + 시간(n을 60으로 나눌때 몫)
#         print('시', end ='')            
#         print(n % 60, end='')            #          분(n을 60으로 나눌때 나머지)
#         print('분', end='')
#         print(' crash')
#                                                                      # trainB trainC 의 교차 
#     elif n % trainB == 0 and n % trainC == 0:                        #  25분   30분     교차 = 150분 간격
#          print('B와 C의 충돌시각은')
#          print(9 + n // 60, end='')      #  9시 + 시간(n을 60으로 나눌때 몫)
#          print('시', end ='')
#          print(n % 60, end='')           #          분(n을 60으로 나눌때 나머지)
#          print('분', end='')
#          print(' crash')
#                                                                      # trainA trainC 의 교차 
#     elif n % trainA == 0 and n % trainC == 0:                        #  10분   30분     교차 = 30분 간격
#          print('B와 C의 충돌시각은')
#          print(9 + n // 60, end='')      #  9시 + 시간(n을 60으로 나눌때 몫)
#          print('시', end ='')
#          print(n % 60, end='')           #          분(n을 60으로 나눌때 나머지)
#          print('분', end='')
#          print(' crash')     
#                                                                      # trainA trainB trainC 의 교차 
#     elif n % trainA == 0 and n % trainB == 0 and n % trainC == 0:    #  10분   25분   30분     교차 = 150분 간격
#          print('A와 B와 C의 충돌시각은')
#          print(9 + n // 60, end='')      #  9시 + 시간(n을 60으로 나눌때 몫)
#          print('시', end ='')
#          print(n % 60, end='')           #          분(n을 60으로 나눌때 나머지)
#          print('분', end='')
#          print(' crash') 


# Quiz) 로그인 기능 만들기
'''
시스템 관리자(admin) 로그인 기능을 만들어봅시다.
관리자가 암호를 입력하고 로그인을 시도할 때 암호가 틀렷다면 '암호를 다시 확인하세요.' 를 출력
암호를 다시 물어봅니다.
5회 이상 로그인에 실패할 경우 '로그인 실패 횟수 초과' 를 출력 후 종료
암호가 정확하하면 '로그인 되었습니다.'를 출력하고 종료함
암호는'dwac1234' 입니다.
'''
# count = 1
# admin_pw = 'dw1234'

# while True:
#     if count > 5:
#         print('로그인 5회 실패로 종료합니다.')
#         break
#     input_pw = (input('암호를 입력하세요.'))
#     if admin_pw == input_pw:
#             print('로그인 되었습니다.')
#             break

#     elif input_pw != admin_pw:
#         print('로그인에 실패하였습니다. 암호를 재 확인하세요.')
#         count += 1

# Quiz) 무한루프에 빠지는것
'''
while True: 
    print('hello') O

while not False: 
    print('hello') O

while 0: 
    print('hello') X

while not 0: 
    print('hello') O
'''

# Quiz) 팩토리얼 만들기
'''
사용자가 입력한 양수를 이용해 팩토리얼 값을 구하는 프로그램
팩토리얼(1) 예시 4! 는 1*2*3*4*
'''
# inputNum  = int(input('양수 입력'))
# result = 1

# for num in range(1,inputNum + 1):
#     result *= num

# print(f'{inputNum}! 는 {result} 입니다.')



# Quiz) Up Down 게임
'''
0부터 100까지의 난수를 발생시키고 사용자가 난수를 맞힐 때까지 물어보는 프로그램
------요구사항------
1부터 100까지의 난수를 발생시켜야함
사용자가 입력하는 숫자가 난수와 일치하면 '정답입니다.'를 출력하고 프로그램 종료.
사용자가 입력하는 숫자가 난수와 불일치시 '틀렸습니다.'를 출력하고 다시물어봄.
입력 제한 횟수는 10회이며 10회를 초과시 '실패했습니다'를 출력하고 프로그램 종료.
입력한 숫자가 다를경우 비교해서 크고 작음을 표기해줌.
게임이 종료될때 정답을 보여줌.
'''

# import random
# attempts = 0
# answer = random.randint(1,100)

# while True:
#     inputAnswer = int(input('정답을 입력하세요.'))
#     attempts += 1
#     print(f'시도한 횟수는{attempts}회 입니다.')
#     if inputAnswer == answer:
#         print('정답입니다.')
#         break
#     else:
#         print('틀렸습니다. 다시맞춰보세요.')

#     if attempts >= 10:
#         print('정답 10회 실패로 사용자가 졌습니다.')
#         print(f'정답은 {answer} 였습니다.')
#         break
#     else:
#         if inputAnswer < answer:
#             print(f'정답은 {inputAnswer} 보다 큽니다.')
#         else:
#             print(f'정답은 {inputAnswer} 보다 작습니다.')


# Quiz) 다음 요구조건을 참고하여 가로와 세로길이의 편화에 따른 사각형의 넓이를 구하는 프로그램
'''
사각형의 넓이는 가로 * 세로
가로길이는 1부터 2의배수로 증가 (1, 2, 4, 6, 8)
세로길이는 1부터 3의배수로 증가 (1, 3, 6, 9, 12)
사각형의 넓이가 150보다 크다면 프로그램 종료
가장 작은사각형과 큰 사각형의 넓이를 출력
'''


# width = 1
# height = 1
# minExtent = width * height
# maxExtent = width * height
# while True:

#     extent = width * height 

#     if width == 1:
#         width = 2
#     else:
#         width += 2

#     if height == 1:
#         height = 3
#     else:
#         height += 3

#     if extent > 150:      
#         break        
#     print(f'사각형의 넓이: {extent} cm^2')
#     if extent < minExtent:
#         minExtent = extent  
                
#     if extent > maxExtent:
#         maxExtent = extent
# print(f'가장 작은 사각형의 넓이는  {minExtent} cm^2')                                       
# print(f'가장 큰 사각형의 넓이는  {maxExtent} cm^2')
































































































































































