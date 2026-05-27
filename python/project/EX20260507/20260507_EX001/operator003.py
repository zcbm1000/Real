# ------------ 논리 연산자
# 논리 연산자는 피연산자의 논리 자료형(T/F)을 이용하는 연산자로 and, or, not 이있음

# and(&) 연산자(모든 조건이 충족해야 True, 하나라도 불 충족시 False)
# 피연산자가 모두 True 인 경우에만 결과가 True임
# 피연산자중 하나라도 False 인 경우 결과는 False임

# var1 = True
# var2 = True
# print(var1 and var2)            # True
# print(var1 & var2)


# var1 = True
# var2 = False  
# print(var1 and var2)            # False
# print(var1 & var2)


# or(|) 연산자 
# 피연산자중 하나 이상의 True가 존재할 경우 True, 피연산자중 전체가 False인 경우 False
# var1 = True
# var2 = True
# print(var1 or var2)             # True
# print(var1 | var2)

# var1 = True
# var2 = False
# print(var1 or var2)             # True
# print(var1 | var2)

# var1 = False
# var2 = False
# print(var1 or var2)             # False


# not 연산자
# 피연산자의 현재상태를 부정하는 연산자(쉽게생각하면 반대로 출력함 True 는 False로, False 는 True로)

# var1 = True
# print(not var1)                   # False 

# var2 = False
# print(not var2)                   # True

# Quiz)
# num1 = 10; num2 = 20; num3 = 30
# result = (num1 < num3) and (num2 < num3)
# print(f'result: {result}')          # True
# # 10<20 True 그리고 20<30 True 두가지 조건을 모두 만족 결과값음 True

# num1 = 10; num2 = 20; num3 = 30
# result = (num1 > num3) and (num2 < num3)
# print(f'result: {result}')          # False 
# # 10>20 False 그리고 20<30 True 두가지 조건을 모두 불 만족 결과값음 False

#-------------and ,or 연산자 사용시 주의사항
# and 연산자는 모든 피연산자가 True인 경우에만 결과를 True로 출력함
# 첫 번째 연산의 결과가 False면 더 이상 연산을 실행 하지않음

# num1 = 10; num2 = 20
# result = (num1 < 15)   and   (num2 > 15)
#              1단계     3단계      2단계  
# 1단계 T 2단게 T 3단게 T  = 결과값음 T
# num1 = 17; num2 = 20
# result = (num1 < 15)   and   (num2 > 15)
#              1단계     3단계      2단계
# 1단계 F 2단계 명령 실행 X

# or 연산자는 피연사중 하나라도 True라면 뒤에 연산자는 무시하고 결과값을 True 출력함
# num1 = 10
#print(f'num1: {num1}')
#print(abc)

# print((num1 > 5)      or      abc)
#         1단계       2단계    3단계
# 1단계에서 True가 나왔기에 2단계로 진행x 결과값을 True로 출력

# Quiz)
# 범퍼카 탑승 가능 판별하는 프로그램
# 신장이 120cm 이상 170미만 인 사람만 탑승이 가능함(가능T, 불가F)

# height = int(input('신장(cm)을 입력하세요.'))
# result = (height >= 120) and (height < 170) 
# print(f'result: {result}')

# ------조건식 == 삼항 연산자
# num1 = 10          # 이항 연산자
# num2 = 10 -5       # 이항 연산자
# not True           # 단항 연산자

targetScore = 90
myScore = 95
# myScore가 targerScore보다 이상이면 합격 미만이면 불합격
# result = '합격' if myScore >= targetScore else '불합격'
# print (f'result ------------------------->{result}')

# Quiz 
# 적자인지 흑자인지 판별하는 프로그램

# incoming = int(input('수입: '))
# outgoing = int(input('지출: '))
# result = '흑자' if incoming > outgoing else '적자'
# print(f'result: {result}')

# Quiz
# 조명장치 자동 on/off 프로그램
# currentLight = 50
# targetLight = 60
# result = 'turn on' if currentLight < targetLight else 'turn off'
# print(f'result: {result}')

