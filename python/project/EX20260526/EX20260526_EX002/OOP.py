# OOP (Object Oriented Programming) | 객체 지향 프로그램

# 객체란 우리주변의 마우스, 자동차, 계산기 와 같은 사물을 뜻함
# 속성(attribue) 과 기능(function) 으로 구성
# 속성은 객체를 구성하는 요소이며, 기능은 해당 객체의 기능을 말함 



# class
# 객체를 생성하기 위한 틀 (설계도)

class FishBread:                       # 클래스 선언

    def __init__(self,f,b):            # 클래스 속성 정의
        self.flour = f                 # 클래스 속성 정의
        self.bean = b                  # 클래스 속성 정의

    def makeFishBread(self):           # 클래스 기능 정의
        print('붕어빵 제조')            # 클래스 기능 정의

# 붕어빵 클래스로부터 객체를 만들어보자.

myFishBread = FishBread('팥', '밀가루')
friendFishBread = FishBread('호박', '쌀가루')


print(f'내 붕어빵의 속: {myFishBread.flour}')        #내 붕어빵의 속: 팥
print(f'내 붕어빵의 반죽: {myFishBread.bean}')       #내 붕어빵의 반죽: 밀가루





# 계산기 클래스
class Calculator:

    # 속성
    def __init__(self, n1, n2):
        self.num1 = n1
        self.num2 = n2

    # 기능
    def add(self):
        print(f'add: {self.num1 + self.num2}')

    def sub(self):
        print(f'sub: {self.num1 - self.num2}')

    def mul(self):
        print(f'mul: {self.num1 * self.num2}')

    def div(self):
        print(f'div: {self.num1 / self.num2}')


myCalculator = Calculator(10, 20)
freindCalculator = Calculator(100, 200)

myCalculator.add()
myCalculator.sub()
myCalculator.mul()
myCalculator.div()

freindCalculator.add()
freindCalculator.sub()
freindCalculator.mul()
freindCalculator.div()



# 인간 클래스 
class Human:
    
    # 속성
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    # 기능
    def walk(self):
        print('걷자')
    def run(self):
        print('달리자')

    def printMyInfo(self):
        print(f'나의 신장: {self.height}')
        print(f'나의 체중: {self.weight}')


human1 = Human(188, 87)
human2 = Human(165, 49)


human1.printMyInfo()
human2.printMyInfo()

human1 = human2
human1.printMyInfo()

human1.height = 200
human1.weight = 39


human2.printMyInfo()