# 할당(대입)연산자
# 할당 연산자는 변수에 값을 대입하는데 사용하는 연산자

# 할당 연산자(=)
num =5         # num 은 5가됨

# 복합대입 연산자(=+, -=, *=, /=, %=, //=, **=)
num = num+5       # num 은 num+5 가됨

num+= 5           # num 은 num+5해서 다시 할당함
num-= 5           # num 은 num-5해서 다시 할당함
num*= 5           # num 은 num*5해서 다시 할당함
num/= 5           # num 은 num/5해서 다시 할당함
num%= 5           # num 은 num%5해서 다시 할당함 
num//= 5          # num 은 num//5해서 다시 할당함
num**= 5          # num 은 num**5해서 다시 할당함

#quiz 복리 계산기
# 5년 예금을 복리(5%)로했을경우 5년후 받을수있는 총 수령액은?

# money = 5000000
# rate = 0.05

# # 1년 후 총 금액
# money = money + (money * rate)

# # # 2년 후 총 금액
# money = money + (money * rate)

# # # 3년 후 총 금액
# money = money + (money * rate)

# # # 4년 후 총 금액
# money = money + (money * rate)

# # # 5년 후 총 금액
# money = money + (money * rate)
 
# print(f'5년 후 총 수령액: {int(money)}원 입니다.')

#---------비교 연산자

# a == b       #a와 b는 같다 
# a != b       #a와 b는 같지않다
# a > b        #a가 b보다 크다
# a < b        #a가 b보다 작다 
# a >= b       #a가 b보다 크거나 같다
# a <= b       #a가 b보다 작거나 같다


# num1 = 10
# num2 = 20
# print(num1 == num2)   #False
# print(num1 != num2)   #True
# print(num1 > num2)    #False
# print(num1 < num2)    #True
# print(num1 >= num2)   #False
# print(num1 <= num2)   #True

# Quiz 범퍼카 탑승 가능여부 판별하는 프로그램
# 놀이동산에서 범퍼카는 신장 120cm 이상만 탑승이 가능합니다.

# height = int(input('신장(cm)을 입력하세요'))
# print(height >= 120)                      # 120이상은 True 120 미만은 False


#---------문자 vs 문자 비교        (아스키코드로변경하여 비교를함)
# print('a' == 'b')       #False         97==98
# print('a'<'b')          #True          97<98
# print('a'>'b')          #False         97>98


#---------문자열 비교
# str1 = 'hello'
# str2 = 'hello'

# print(str1 == str2)        #True
# print(str1 != str2)        #False

#---------문자열 비교(공백도 문자로인식)
# str1 = 'hello'
# str2 = 'hello '

# print(str1 == str2)        #False
# print(str1 != str2)        #True

#---------