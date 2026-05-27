# split  쪼갠다의 의미

# names = ('박찬호', '이승엽', '박세리', '박지성', '이순철', '선동열', '손흥민', '김연아')
# print(f'names: {names}')
# print(f'names: {type(names)}')

# str = '박찬호A이승엽A박세리A박지성A이순철A선동열A손흥민A김연아'
# splitStr = str.split('A')                  # str 을 A로 쪼개서 다시담아줌
# print(splitStr)                            # 리스트가됨 ['박찬호' ~ '김연아']
# print(f'splitStr_type: {type(splitStr)}')  # 타입이 리스트임


# str = '박찬호A이승엽A박세리A박지성A이순철A선동열A손흥민A김연아'
# splitStr = str.split('A')                  # str 을 A로 쪼개서 다시담아줌
# splitStr = tuple(splitStr)                 # splitStr 을 튜플로 만듬
# print(splitStr)                            # splitStr 을 출력
# print(f'splitStr_type: {type(splitStr)}')  # 튜플로 출력





# 튜플 안의 아이템 유/무 확인하기
# in 과 not in 을 사용하면 튜플안의 특정아이템의 존재 유/무를 확인할수있음 유:True, 무:False

# colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')
# print(f'{'Green' in colors}')    # colors 안에 'Green' 이라는 아이템이 있으면 True


# if 'Green' in colors:
#     print(f'colors 에는 Green 이 있습니다')
# else:
#     print(f'colors 에는 Green 이 없습니다')



# colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')
# print(f'{'Green' not in colors}')    # colors 안에 'Green' 이라는 아이템이 있으면 False


# if 'Green' not in colors:
#     print(f'colors 에는 Green 이 없습니다')
# else:
#     print(f'colors 에는 Green 이 있습니다')


# Quiz) 학점 경고 프로그램
'''
socres는 1학기 성적을 튜플로 나타낸것입니다.
F 학점이 있다면 '경고'를 출력하는 프로그램
'''

# scores = ('A', 'B', 'A', 'C', 'C' )
# if 'F' in scores:
#     print('경고')
# else:
#     print('경고없음')
    

# scores = ('A', 'B', 'A', 'F', 'C' )
# if 'F' in scores:
#     print('경고')
# else:
#     print('경고없음')

# scores = ('A', 'C', 'F', 'B', 'A', 'F', 'C' )
# fCnt = scores.count('F')
# print(f' F의 갯수는: {fCnt}')


# num1 = (1, 2, 3)
# num2 = (4, 5, 6)

# num1.extend(num2)          # 불가함 extend 는 원본데이터가 확장되는데 확장이되면 원본데이터의 변형이 발생
# print(num1)

# num3 = num1 + num2           # +의 경우는 num1 과 num2 의데이터를 복사하여 num3에 붙여놓은거기에
# print(num3)                  # num1 과 num2 의 데이터는 변형없이 보존되기에 가능함




# nums1 = [1,2,3]
# nums2 = nums1

# for idx, num in enumerate(nums1):
#     nums2[idx] = num

# print(f'nums1: {nums1}')
# print(f'nums2: {nums2}')

# nums1[0] = 100
# print(f'nums1: {nums1}')
# print(f'nums2: {nums2}')

# import copy

# a = [1, 2, 3, 4, 5]
# b = copy.deepcopy(a)            # b = a 는 얕은 복사(주소값만 복사)에해당
#                                 # a 는 데이터 자체를 카피 데이터가 새로 생김 (깊은복사)  
# b[0] = 100

# print(f' a : {a}')
# print(f' b : {b}')

# nums1 = [1,2,3]
# nums2 = [0,0,0]

# for idx, num in enumerate(nums1):
#     nums2[idx] = num

# print(f'nums1: {nums1}')
# print(f'nums2: {nums2}')

# nums1[0] = 100
# print(f'nums1: {nums1}')
# print(f'nums2: {nums2}')


# 슬라이싱
# animals = ('호랑이', '사자', '곰', '여우', '늑대')  # 튜플 지정
# print(f'animals: {animals}')                       # animals: ('호랑이', '사자', '곰', '여우', '늑대')

# print(f'animals[:3]: {animals[:3]}')               # animals[:3]: ('호랑이', '사자', '곰')
# print(f'animals[1:4]: {animals[1:4]}')             # animals[1:4]: ('사자', '곰', '여우')

# print(f'animals[:-2]: {animals[:-2]}')             # animals[:-2]: ('호랑이', '사자', '곰')
# print(f'animals[-3:-1]: {animals[-3:-1]}')         # animals[-3:-1]: ('곰', '여우')






# Quiz)
'''
fruits 튜플에서 주어진 요구사항에 맞게 슬라이싱해봅시다.
fruits = ('apple', 'banana', 'plum', 'watermelon', 'peach')
 - 인덱스 2부터 4까지의 아이템을 출력하시오.
 - 인덱스 0부터 3까지의 아이템을 출력하시오.
 - 인덱스 3부터 끝까지의 아이템을 출력하시오.
'''
# fruits = ('apple', 'banana', 'plum', 'watermelon', 'peach')
# print(f'fruits[2: ]: {fruits[2: ]}')            # fruits[2: ]: ('plum', 'watermelon', 'peach')
# print(f'fruits[ :4]: {fruits[ :4]}')            # fruits[ :4]: ('apple', 'banana', 'plum', 'watermelon')
# print(f'fruits[3: ]: {fruits[3: ]}')            # fruits[3: ]: ('watermelon', 'peach')
   

# 리스트와 튜플간 변환(형변화)
'''
불가피하게 튜플의 아이템을 수정하려면 리스트로 변환해야함
또한 리스트로 선언된 데이터를 수정이 안되게 하려면 튜플로 변환해야함
다음은 데이터 변환을 통해 리스트와 튜플을 변환하고있음
'''

# # colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')     # 튜플
# # Orange 라는 아이템을 '오렌지'로 바꾸고싶음
# # colors[1] ='오렌지'                      # 튜플이기에 데이터변환이 불가
# colors = list(colors)                      # 데이터 타입이 튜플에서 리스트로 변환됨
# print(f'colorsType: {type(colors)}')       # 출력 colorsType: <class 'list'>

# colors[1] = '오렌지'                       # 리스트 1번인덱스 orange 를 '오렌지'로 바꿈
# print(f'colors: {colors}')                 # 출력 colors: ['Red', '오렌지', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple']

# colors = tuple(colors)                     # 데이터 타입이 리스트에서 튜플로 변환됨
# print(f'colorsType: {type(colors)}')       # 출력 colorsType: <class 'tuple'>

# Quiz) 튜플 정렬하기

# colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')
# print(f'기존colors: {colors}')
# colors = list(colors)

# colors.sort()

# colors = tuple(colors)

# print(f'정렬된colors: {colors}')
# print(f'colorsType: {type(colors)}')   


# colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')

# sc = tuple(sorted(colors))     # sort 를 해줌 (타입변환 안할경우)타입이 튜플이 아닌 리스트됨
# print(f'sc: {sc}')


















































































































































