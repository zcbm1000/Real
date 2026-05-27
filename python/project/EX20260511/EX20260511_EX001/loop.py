 # 반복문 #for문 & while문) 

#for 문:  ~하는동안  → 횟수에 의한 반복
#ex) 국에 소금을 넣는다면 5번넣는다면 for문(5번이라는 횟수를 정하였기에)

#while문: ~하는동안  → 횟수에 의한 반복
#ex) 국에 소금을 넣는다면 싱거워지지 않을때까지 넣는다면 while문(국이 싱거워지지않을때 까지라는 조건을 정하였기에)


# for문: ~하는동안  → 횟수에 의한 반복

'''
for 변수 in 범위:
for 'A' in range(부터,까지{+1수치},간격)
    실행할 문장
'''

'''
for
'''

# 1~10까지 출력하기
# for num in range(1,11):
#     print(f'{num} : hello')

# # 1~10까지 (1,3,5,7,9) 출력
# for a in range (1,11,2):
#     print(a)

# 0부터 10까지 정수출력           # 0부터 10까지의 정수중
# for a in range(0,11,1):         # 0부터 10까지의 정수중 1단계씩 증가하는 수를
#     print(a)                    # 출력 → 0,1,2,3,4,5,6,7,8,9,10


# range() 간략화 (단계가 1인경우에만 생략이 가능함 a(시작),b(종료),c(단계))
#                 단계가  생략되고 시작이 0인경우는 시작도 생략이 가능함

# for a in range(0,11):         # 단계 생략
#     print(a)

# for a in range(11):           # 단계 생략, 시작 생략
#     print(a)

# for a in range(2,9,2):        # 2부터 9사이에 잇는 숫자중 2씩 증가하는 숫자 출력
#     print(a)

# Quiz) 2~8 사이의 짝수만 출력하기

# for num in range(1,16):                  # 1부터 15까지의 숫자 중
#     if num % 2 == 0 and num <= 8:        # 8이하의 숫자에서 2로 나누엇을때 0이 되는 수
#         print(num)                       # 출력 → 2,4,6,8




# Quiz) 사용자가 입력한 횟수만큼 '메일 발송' 문자열을 출력하기 
# printCount = int(input('출력 횟수를 입력하세요.'))
# for count in range(1, printCount+1):
#     print(f'{count} : 메일발송')



# Quiz) 1과 10사이의 정수를 출력하되, 정수가 3의 배수이면 '3의 배수'라고 출력하기

# for num in range(1,11):                        # 1부터 10까지 숫자중
#     if num % 3 ==0:                            # 3으로 나누엇을떄 0이되는수는
#         print(f'{num} : 3의 배수!')            # 뒤에 : 3의 배수!" 를 출력함
#     else: print(num)                           # 그렇지 않다면 숫자를 출력함

# for num in range(1,11):                        # 1부터 10까지 숫자중
#     print(f'{num} : 3의 배수!') if num % 3 ==0 else print(num)  # 3으로 나누엇을떄 0이되는수는 뒤에 : 3의 배수!" 를 출력함, 그렇지 않다면 숫자를 출력함


# QUiz) 사용자가 원하는 구구단을 입력하면 해당 구구단을 출력
# multiPlication = int(input('원하는 구구단을 입력하세요.'))             # 원하는 구구단의 단수를 입력
# for num in range(1,11):                                               # 1부타 10까지의 숫자중
#     print(f'{multiPlication} * {num} = {multiPlication*num}')         # 입력한 구구단의 단수와 숫자를 곱함 = 숫자로 출력


# Quiz) 1부터 10까지 정수의 합을 출력하세요.

# inputNum = int(input('숫자를 입력하세요.'))

# for num in range(1,11):                                   # 1부터 10까지의 숫자중
#     print (f'{inputNum} 까지의 합은 {sum(range(1,inputNum+1))}')
           


# Quiz) for 문을 이용하여 1부터 100까지의 정수중 3과 7의 공배 최소공배수를 출력하세요.

# first = True

# for num in range(1,101):
#     if num % 3 == 0 and num % 7 == 0 and first == True:            
#         print(f'3,7의 최소 공배수 = {num}')
#         first = False
#     elif num % 3 == 0 and num % 7 == 0:
#         print(f'3,7의 공배수 = {num}')


# minNum = 0
# for num in range(1,101):                 # 1부터 100까지의 숫자중
#     if num % 3 == 0 and num % 7 == 0:    # num을 3으로 나누었을때 0인것 그리고 num을 7로 나누었을때 0인것은
#         print(f'3,7의 공배수 = {num}')   # 3과 7의 공배수는 num으로 출력함
#         if minNum == 0: minNum = num     # minNum이 0이라면 minNum에 num을 할당함 → 최초의 공배수는 최소 공배수가 됨
# print(f'3,7의 최소 공배수 = {minNum}')   # 3과 7의 최소 공배수는 minNum으로 출력함


# 문자열을 이용한 for문
# for tk in 'hello':             # 문자열 'hello' 의 각 한글자씩 tk에 할당하여 반복
#     print(f'tk: {tk}')         # tk: h, tk: e, tk: l, tk: l, tk: o 



# Quiz) 50보다 작은 7의 배수를 출력하는 프로그램
# for num in range(1,51):            # 1부터 50까지의 숫자중
#     if num % 7 == 0:               # num을 7로 나누엇을때 0이되는 수는
#         print(f'num: {num}')       # "num: ??" 출력


# While문: ~하는동안  → 조건에 의한 반복(조건이 참이면 실행, 거짓이면 종료)
# while 조건: while True:  # 조건이 참인 동안 반복
#     실행할 문장 << 조건이 참인 동안 반복할 문장
#                    조건이 거짓이 되면 반복 종료
# 무한루프에 빠지지 않도록 주의해야함
#ex) num = 1           # num은 1로 초기화
# while num < 10:   # num이 10보다 작은 동안 반복
#     print(num)    # num을 출력함
# 위의경우는 num 은계속 1이기때문에 10보다 작음 → 무한루프에 빠짐



# num = 1           # num은 1로 초기화
# while num < 10:   # num이 10보다 작은 동안 반복
#     print(num)    # num을 출력함
#     num += 1      # num에 1을 더하여 num에 재 할당함 → num이 10이 될때까지 반복함


# num = 1                     # num은 1로 초기화
# while num <= 10:            # num이 10보다 작거나 같은 동안 반복
#     print(f'num: {num}')    # num을 출력함
#     num += 1                # num에 1을 더하여 num에 재 할당함 → num이 10이 될때까지 반복함



#Quiz) 1부터 30까지의 정수 중 홀수와 짝수를 구분하여 출력
# num = 1
# while num < 31:                               # num이 31보다 작은 동안 반복
#     if num % 2 == 0:                          # num을 2로 나누었을때 0이 되는 수는
#         print(f'num: {num} 짝수입니다.')      # "num: ?? 짝수입니다." 출력
#     else:                                     # 그렇지 않다면
#         print(f'num: {num} 홀수입니다.')      # "num: ?? 홀수입니다." 출력
#     num += 1                                  # num에 1을 더하여 num에 재 할당함 → num이 30이 될때까지 반복함



# num = 1
# while num < 31:                               # num이 31보다 작은 동안 반복
#     if num % 2 == 0:                          # num을 2로 나누었을때 0이 되는 수는
#         print(f'num: {num} 짝수입니다.')      # "num: ?? 짝수입니다." 출력
#     else:                                     # 그렇지 않다면
#         print(f'num: {num} 홀수입니다.')      # "num: ?? 홀수입니다." 출력
# num += 1                                      # num에 1을 더하여 num에 재 할당함 → num이 30이 될때까지 반복함


# Quiz) 구구단 3단 출력하기 while문을 사용
# num = 1
# while num < 13:                                  # num이 13보다 작은동안 반복
#     if num % 3== 0:                              # num % 3 == 0 num 을 3으로 나누었을때 0이되는 수는
#        print(f'3 * {num//3} = {num}')            # "3 * ?? = ??" 출력 (num//3은 num을 3으로 나눈 몫을 출력함)
#     num += 1                                     # num에 1을 더하여 num에 재 할당함 → num이 12가 될때까지 반복함


# multiplication = int(input('원하는 구구단을 입력하세요: '))
# num = 1
# while num < 13:                                  # num이 13보다 작은동안 반복
#     if num % multiplication == 0:              # num % multiplication == 0 num 을 multiplication으로 나누었을때 0이되는 수는
#        print(f'{multiplication} * {num//multiplication} = {num}')            # "{multiplication} * ?? = ??" 출력 (num//multiplication은 num을 multiplication으로 나눈 몫을 출력함)
#     num += 1                                     # num에 1을 더하여 num에 재 할당함 → num이 12가 될때까지 반복함



# Quiz) 구구단 전체(2단~9단) 을 출력

# multiplication = 2                                                   # multiplication은 2로 해당(단수에해당)
# while multiplication < 10:                                           # 9단까지 반복
#     print(f'{multiplication}단')                                     # "단수" 출력
#     num = 1                                                          # num은 1로해당(곱할수에 해당함)
#     while num < 10:                                                  # num이 10보다 작은동안 반복
#         print (f'{multiplication} * {num} = {multiplication*num}')   # print 단수 * 곱할수 = 결과
#         num += 1                                                     # num에 1을 더하여 num에 재 할당함(10까지) 
#     multiplication += 1                                              # multiplication에 1을 더하여 multiplication에 재 할당함(10까지)
 
# multiplication = 1                                                     # multiplication은 1로 해당(단수에해당)
# while multiplication < 10:                                             # 9단까지 반복
#     for multiplication in range(2,10):                                 # multiplication이 2부터 9까지의 숫자중
#         print(f'{multiplication}단')                                   # "단수" 출력
#         for num in range(1,10):                                        # num이 1부터 9까지의 숫자중
#             print(f'{multiplication} * {num} = {multiplication*num}')  # print 단수 * 곱할수 = 결과
#         multiplication += 1                                            # multiplication에 1을 더하여 multiplication에 재 할당함(10까지)



# Quiz) 구구단을 출력하나 가로로 출력 



# multiplication = 2                                                            # multiplication은 2로 해당(단수에해당)
# while multiplication < 10:                                                    # 9단까지 반복
#     print(f'{multiplication}단')                                              # "단수" 출력
#     print()                                                                  
#     num = 1                                                                   # num은 1로해당(곱할수에 해당함)
#     while num < 10:                                                           # num이 10보다 작은동안 반복
#         print (f'{multiplication} * {num} = {multiplication*num}')            # print 단수 * 곱할수 = 결과
#         num += 1                                                              # num에 1을 더하여 num에 재 할당함(10까지) 
#     multiplication += 1
#     print()    

# multiplication = 2
# while multiplication < 10:
#     print(f'{multiplication}단', end = '              ')
#     multiplication += 1
# num = 1
# while num < 10:
#     for multiplication in range(2,10):
#         print(f'{multiplication} * {num} = {multiplication*num}', end = '    ')
#     print()
#     num += 1




# Quiz) while문을 이용하여 0~100까지 정수중 3과 8의 공배수와 최소 공배수를 출력
# num = 1                                                     # num 을 1로 지정
# minimum = 0                                                 # m
# while num <101:                                             # num 
#     if num % 3 == 0 and num % 8 == 0:
#         print(f'3과8의 공배수: {num}')
#         if minimum == 0:
#             minimum = num
#     num += 1
# print(f'3과 8의 최소공배수는 {minimum} 입니다.')


# 반복문 내 실행 제어(continue, break)

# continue
# 반복문(for, while)에 continue 키워드를 사용하면 이후 실행을 생략하고 다시 반복문의 처음으로 돌아감.

# continue 를 이용하여 1부터 10까지의 정수 중 홀수만 출력하는 프로그램
# for num in range(1,11):                # 1~10까지를 num에 할당함
#     if num % 2 == 0:                   # num 을 2로나누엇을때 0이라면(짝수라는소리) 
#         continue                       # continue 제끼고 위로올림
#     print(f'num: {num}')               # 출력함(짝수를 제꼇기에 홀수만 출력을함)

# break
# 반복문(for, while)에 break 키워드를 사용하면 실행을 즉시 중단하고 반복문을 빠져나옴

# break 를 이용하여 1부터 10까지의 숫자를 더하되 결과가 30이상이 될 때 정수를 찾는 프로그램
# num = 1                    # num에 1을 할당
# sum = 0                    # sum에 0을 할당
# while num < 11:            
#     sum += num                             
#     if sum >= 30:                          # sum이 30 이상이될때
#         print(f'num: {num}')               # 넘아가는 숫자를 측정
#         break                              # 실행 중단
#     num += 1


# count = 1                                  # count에 1을 할당함
# for num in range(1,10,1):                      # num은 1부터 10까지
#     print(f'num: {num}')                   # 출력
#     count += 1                             # count 에 1을 추가해서 재 할당함
#     if count >= 5:                         # count가 5 이상이 될경우(1,2,3,4)
#         break                              # 실행 중단


# for ~ else 키워드
'''
for문에 else 키워드를 사용하는 경우, else 이하의 구문을 for문의 반복 업무를 모두 완료하고 난 후 실행
'''

# 1부터 5까지의 정수를 출력하고 반복문이 종료되면 완료 메시지를 출력
# for num in range(1,6):
#     print(f'num: {num}')
# else:    
#     print('완료되었습니다.')

# 위 문구와 아래 문구는 출력 내용은 동일함.

# for num in range(1,6):
#     print(f'num: {num}')
# print('완료되었습니다.')

# pass 키워드
# for num in range(1,10):     # 1부터 9까지 num에 할당함
#     pass                    # pass 실행을 하지않고 건너뜀(코드가 미 완성이어도 오류가 발생하지 않음)


# Quiz) 삼각형의 넓이 구하기
'''
가로 길이와 세로 길이의 변화에 따른 삼각형의 넓이를 구하는 프로그램
가로 길이는 1부터 2의 배수로 증가
세로 길이는 1부터 3의 배수로 증가
삼각형의 넓이가 150보다 크면 프로그램을 종료
'''

# count = 1
# maxArea = 150

# while True:                                           # 무한 반복문 break 가 나오기 전까지 반복을함
#     result = ((count *2) * (count * 3)) / 2           # result = (2c *3c / 2) 값
#     if result > 150: break                            # result가 150보다 커지면 중단
#     print(f'삼각형의 넓이: {result} cm^2')             # 삼각형의 넓이: 결과cm^2 출력 
#     count += 1                                        # count 에 1씩 추가를 해서 계속 연산을함



# Quiz) 1부터 시작해서 숫자를 계속 더하다가 합이 50을 넘으면 멈추는 프로그램

# num = 1                                        # num 에 1을 할당
# total = 0                                      # total에 0을 할당
# while total < 50:                              # total이 50 미만이 될때까지
#     total += num                               # total에 num을 더해서 재 할당
#     print(f'더한 수는: {num}, 합계: {total}')   # 출력(더한수는: 숫자 , 합계: 전체)
#     num += 1                                   # num에 1을 더해서 재 할당



# total = 0                                         # 전체값에  0 을 할당함
# while total < 31:                                 # 전체값이 31보다 작을때까지
#     num = int(input("더할 숫자를 입력하세요: "))   # 숫자는 사용자가 직접 입력함 
#     total += num                                  # 숫자를 더한 값을 전체에 재 할당함
#     print(f'입력한 수: {num}, 합계: {total}')      # 출력

