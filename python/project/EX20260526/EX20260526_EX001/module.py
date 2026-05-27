# 자주 사용하는 모듈: 내장 모듈
# 내장 모듈은 외우는것이 아님.
# 따라서 가볍게 훑어보고 필요할때 찾아서 사용

# ---------------------------------------------------------------

# math 모듈: 수학 함수와 관련된 모듈
'''
fabs()     : 절댓값을 반환
ceil()     : 소수점 이하 올림한 값을 반환
floor()    : 소수점 이하 내림한 값을 반환
trunc()    : 소수점 이하 버림한 값을 반환
gcd()      : 최대 공약수를 반환
sqrt()     : 제곱근을 반환
factorial(): 팩토리얼한 값을 반환

'''

# import math

# print(f'{math.fabs(3.1415)}')      # 3.1415
# # 절댓값을 반환 

# print(f'{math.ceil(3.1415)}')      # 4
# # 소수점 이하 올림한 값을 반환

# print(f'{math.floor(3.1415)}')     # 3
# # 소수점 이하 내림한 값을 반환

# print(f'{math.trunc(3.1415)}')     # 3
# # 소수점 이하 버림한 값을 반환

# print(f'{math.gcd(7, 21)}')        # 7
# # 최대 공약수를 반환 

# print(f'{math.sqrt(3.1415)}')      # 1.772427713617681
# # 제곱근을 반환

# print(f'{math.factorial(4)}')      # 24
# # 팩토리얼한 값을 반환

# ---------------------------------------------------------------

# 파이썬 내장 함수중에서 수학과 관련한 함수
'''
sum()  : 전체 합을 반환
max()  :
min()  :
abs()  :
pow()  : 거듭 제곱을 반환
round(): 반올림한 값을 반환
'''

# ---------------------------------------------------------------

# random 모듈: 난수를 발생시키는 모듈
'''
random(): 0이상 1미만의 난수를 발생
randint(n1, n2): n1 이상 n2 이하의 난수를 발생
randrange(n1, n2): n1이상 n2 미만의 난수를 발생
sample(range(n1, n2), n3): n1 이상 n2 미만의 난수중 n3개의 난수 발생(중복 X)
choice(): 무작위로 1개 아이템을 선택
shuffle(): 아이템 순서 섞음

'''

# import random
# print(f'random: {random.random()}')
# # 0 이상 1 미만의 난수를 발생

# print(f'randint: {random.randint(0, 9)}')
# # 0 이상 9 이하의 난수를 발생

# print(f'randrange: {random.randrange(0, 9)}')
# # 0 이상 9 미만의 난수를 발생

# print(f'sample: {random.sample(range(0, 9), 3)}')
# # 0 이상 9 미만의 난수중 3개의 난수 발생(중복 X)

#---------------------------------------------------------------

# listVar = [1, 2, 3, 4, 5]

# print(f'choice: {random.choice(listVar)}')
# # 무작위로 1개 아이템을 선택

# random.shuffle(listVar)
# print(f'shuffle: {listVar}')
# # 아이템 순서 섞음

# ---------------------------------------------------------------

# time 모듈: 시간 관련 모듈(UTC)
'''
localtime(): 시스템의 현재 시간을 반환
gmtime(): GMT 시간을 반환
strftime(): 시간 포맷 코드에 따른 출력

'''

import time


lt = time.localtime()          # 시스템 시간
print(f'localtime: {lt}')      

print(f'년도: {lt.tm_year}')    # 시스템 시간의 연도 출력
print(f'월: {lt.tm_mon}')
print(f'일: {lt.tm_mday}')
weekday = ['월 요일', '화 요일', '수 요일', '목 요일', '금 요일', '토 요일', '일 요일']

print(f'일: {lt[lt.tm_wday]}')

gmtTime = time.gmtime()

print(f'gmtTime: {gmtTime}')

print(f'gt.tm_hor: {gmtTime.tm_hour}')

print(f'시: 분: 초: {time.strftime("%H:%M:%S", time.localtime())}')








































































































































































































































































































