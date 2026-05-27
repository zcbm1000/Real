# Quiz) 영수증을 만들어주는 프로그램
'''
상품가격 표를 보고 영수증을 출력해보자
상품 갯수는 사용자가 직접 입력한다.
새우깡:   1200
비비빅:   400
맛동산:   1500
초코파이: 500

새우깡 2개, 비비빅 3개, 맛동산 4개, 초코파이 1개 구매
'''

goods = {'새 우 깡': 1200,
         '비 비 빅': 400,
         '맛 동 산': 1500,
         '초코파이': 500       
}
totalPrice = 0

def shrimpCrackerPrice():
    global totalPrice
    price = goods["새 우 깡"] * shrimpCracker
    totalPrice += price
    print(f'새 우 깡 구매 금액: {goods['새 우 깡'] * shrimpCracker}')

def redBeanIcebarPrice():
    global totalPrice
    price = goods["비 비 빅"] * redBeanIcebar
    totalPrice += price
    print(f'비 비 빅 구매 금액: {goods['비 비 빅'] * redBeanIcebar}')

def matDongSanPrice():  
    global totalPrice
    price = goods["맛 동 산"] * matDongSan
    totalPrice += price
    print(f'맛 동 산 구매 금액: {goods['맛 동 산'] * matDongSan}')

def chocoletPiesPrice(): 
    global totalPrice
    price = goods["초코파이"] * chocoletPies
    totalPrice += price         
    print(f'초코파이 구매 금액: {goods['초코파이'] * chocoletPies}')
    

shrimpCracker = int(input('새 우 깡 구매 개수를 입력하세요: '))
redBeanIcebar = int(input('비 비 빅 구매 개수를 입력하세요: '))
matDongSan    = int(input('맛 동 산 구매 개수를 입력하세요: '))
chocoletPies  = int(input('초코파이 구매 개수를 입력하세요: '))

print(f'새 우 깡 구매 갯수 : {shrimpCracker}')
print(f'비 비 빅 구매 갯수 : {redBeanIcebar}')
print(f'맛 동 산 구매 갯수 : {matDongSan}')
print(f'초코파이 구매 갯수 : {chocoletPies}')

print('=' * 40)

shrimpCrackerPrice()
redBeanIcebarPrice()
matDongSanPrice()
chocoletPiesPrice()

print('=' * 40)
print(f'총 금액은 {totalPrice}')



