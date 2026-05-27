# ----------------- 모듈
'''
모듈이란 특정 기능을 모아놓은 파일로 모듈을 이용하면 우리가 직접 코딩해야하는 수고를 덜을수 있음
예를들어 random 모듈은 난수를 발생시키는 기능을 가지고있음
만약 random 모듈을 사용하지않고 난수를 직접 발생시키려면 직접 프로그램을 작성해야함

모듈을 사용하려면 우선 import를 이용해 모듈을 가지고 와야함
다음은 random 모듈을 이용해 로또에 필요한 난수를 발생시키는 코드임
'''

import random
randomNum = random.randrange(1,46)
print(f'randomNum:{randomNum}')

# + - * / 기타등등을 모아둔 모듈 > operator 모듈(연산자 모듈)

import operator
print(20+10)
#모듈 없이 했던방식
print (operator.add (20,10))
#모듈 사용 방식

print(20-10)
#모듈 없이 했던방식
print (operator.sub (20,10))
#모듈 사용 방식

print(20*10)
#모듈 없이 했던방식
print (operator.mul (20,10))
#모듈 사용 방식

print(20/10)
#모듈 없이 했던방식
print (operator.truediv (20,10))
#모듈 사용 방식

print(20%10)
#모듈 없이 했던방식
print (operator.mod (20,10))
#모듈 사용 방식

print(20//10)
#모듈 없이 했던방식
print (operator.floordiv (20,10))
#모듈 사용 방식

print(20**10)
#모듈 없이 했던방식
print (operator.pow (20,10))
#모듈 사용 방식

print(20==10)
#모듈 없이 했던방식
print (operator.eq (20,10))
#모듈 사용 방식

print(20!=10)
#모듈 없이 했던방식
print (operator.ne (20,10))
#모듈 사용 방식

print(20>10)
#모듈 없이 했던방식
print (operator.gt (20,10))
#모듈 사용 방식

print(20>=10)
#모듈 없이 했던방식
print (operator.ge (20,10))
#모듈 사용 방식

print(20<10)
#모듈 없이 했던방식
print (operator.lt (20,10))
#모듈 사용 방식

print(20<=10)
#모듈 없이 했던방식
print (operator.le (20,10))
#모듈 사용 방식

print(True and False)
#모듈 없이 했던방식
print (operator.and_ (True,False))
#모듈 사용 방식

print(True or False)
#모듈 없이 했던방식
print (operator.or_ (True,False))
#모듈 사용 방식
print(not False)
#모듈 없이 했던방식
print (operator.not_ (False))
#모듈 사용 방식