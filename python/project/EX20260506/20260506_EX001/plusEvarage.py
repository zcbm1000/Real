#변수 활용하여 사용

firstNum = int(input('첫번째 정수를 입력하세요.'))
secondNum = int(input('두번째 정수를 입력하세요.'))

sum= firstNum+secondNum
AVG = sum/2

print(f'합: {sum}')
print(f'평균: {AVG}')


# 변수 없이 사용하는법

firstNum = int(input('첫번째 정수를 입력하세요.'))
secondNum = int(input('두번째 정수를 입력하세요.'))

print(f'합: {firstNum+secondNum}')
print(f'평균: {(firstNum+secondNum)/2}')
