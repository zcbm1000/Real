# Quiz) 단위 환산 프로그램
'''
mm 당위의 길이를 입력하면 cm, m, inch, ft 로 단위가 변환되어 출력되는 프로그램
함수를 이용할것
1센티는 10밀리미터
1센티는 0.01 미터
1센티는 0.39 인치
1센티는 0.03 피트

'''

def coverUnit(lenMm):
    unitDic = {}

    unitDic['cm'] = lenMm * .1
    unitDic['m'] = lenMm * .001
    unitDic['inch'] = lenMm * .03931
    unitDic['ft'] = lenMm * .003281

    return unitDic

def pringLength(lengths):
    for len in lengths.keys():
        print(f'{len}: {lengths[len]}{len}')
inputData = int(input(f'길이(mm)를 입력하세요.\n 입력:'))
resultData = coverUnit(inputData)
printLength = (resultData)


# Quiz) 할인된 상품 가격표 출력 프로그램
'''
마트는 고객 감사의 일환으로 '오늘의 할인' 이벤트를 진행할 계획이다.
아래의 상품 가격표를 참고해서, '오늘의 할인율' 을 입력하면 
할인된 가격이 출력되는 프로그램

쌀  : 9900
상추: 1900
고추: 2900
마늘: 8900
통닭: 5600
햄  : 6900
치즈: 3900
'''

# standardPrice = {
#     '쌀' : 9900,
#     '햄' : 6900,
#     '상추': 1900,
#     '고추': 2900,
#     '마늘': 8900,
#     '통닭': 5600,
#     '치즈': 3900
# }

# def getDiscountPrice(rate):
#     dcPrice = {}
#     for goodsName in standardPrice.keys():
#         disPrice = int(standardPrice[goodsName] * (1 - (rate / 100)))
#         dcPrice[goodsName] = disPrice

#     return dcPrice

# def printPrice(priceList): 01
#     for goodsName, goodsPrice in priceList.items():
#         print(f'{goodsName}: {standardPrice[goodsName]}--->{inputData}%DC하여 {goodsPrice}입니다.')

# inputData = int(input('오늘의 할인율을 입력하세요:\n할인율:'))

# discountPrice = getDiscountPrice(inputData)

# printPrice(discountPrice)

    

# QUiz) 영어 사전

# englishDictionary = {
#     'apple': '사과',
#     'chair': '의자',
#     'doll' : '인형',
#     'book' : '책',
#     'piano': '피아노',
#     'clock': '시계'
# }

# def printWord(englishWord):
#     print(englishDictionary[englishWord])

# printWord(input('찾고자 하는 영어 단어 입력: '))    






 