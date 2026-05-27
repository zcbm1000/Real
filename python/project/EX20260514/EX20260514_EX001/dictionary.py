

# dictionary(딕셔너리)
'''
딕셔너리(dictionary)는 리스트와 함께 파이썬 프로그램에서 많이 사용하는 컨테이너 자료형입니
다. 리스트가 인덱스를 이용하여 아이템을 참조한다면, 딕셔너리는 인덱스 대신 키(key)를 이용하
여 아이템을 참조(관리)합니다. 
'''

# 딕셔너리는 키(key) 와 값(value)로이루어져잇음
# 딕셔너리는 인덱스대신 키를이용함.
# 리스트의 인덱스는 자동생성이나 딕셔너리의 키는 직접입력해야함.
# 3개의 사물함이있음 (값은 사물함이된)
# 3개의 사물함에는 각 맞는 열쇠가 있음(key)
# 1번 열쇠는 1번 사물함만 열수있음

# 딕셔너리 정의
# 딕셔너리는 {} 이용함 | 리스트는 [] | 튜플은 ()

# 키 값은 절대! 중복 되면 안된다.
# 밸류 값은 상관 없음.

# #      |   키   밸류 |   키   밸류 |   키   밸류 |   키   밸류 |  키   밸류 |
# ages = {'박찬호': 48, '박지성': 40, '박세리': 50, '이승열': 43, '박지성': 50}
# print(f'ages: {ages}')
# print(f'ages type: {type(ages)}')

# scores = {
# 'c/c++'  : 'A', 
# 'java'   : 'B+',
# '네트워킹': 'C',
# '보안'    : 'A+',
# '해킹'    : 'F',
# '시스템'  : 'C+'
# }

# print(f'scores: {scores}')


# 리스트, 튜플, 딕셔너리

# listVar = [3, 3.15, 'hell']
# print(f'listVar: {listVar}')

# tupleVar = [3, 3.15, 'hell']
# print(f'tupleVar: {tupleVar}')

# dictVar = {
#     '홍길동': 10,
#     '박찬호': '열살',
#     '박세리': 3.14
# }
# print(f'dictVar: {dictVar}')


# listVar1 =[1, 2, 3]
# listVar2= [1, 2, 3, listVar1]

# print(f'listVar1: {listVar1}')       # listVar1: [1, 2, 3]                  
# print(f'listVar2: {listVar2}')       # listVar2: [1, 2, 3, [1, 2, 3]]  
# print(listVar2[3][1])                # listvar2[1, 2, 3, [1, 2, 3]] 에있는 
#                                      # 인덱스값 3 [listVar1] 이 나오는데 그중 인덱스값 1을
#                                      # 출력하면 listVar1[1, 2, 3] 중 인덱스 1은 2가 됨
# print(type(listVar2[3]))             # type 은 list
# print(type(listVar2[3][1]))          # type 은 int


# dicts ={
#     'name' : '박찬호',
#     'age'  : 20,
#     'addr' : '대전 중구',
#     'hobby': ['축구', '농구', '배구']
# }
# print(f'dicts: {dicts}')
# ''' 출력하면 다음과 값이 같음 
# dicts: {'name': '박찬호', 'age': 20, 'addr': '대전 중구', 'hobby': ['축구', '농구', '배구']}
# '''

# print(dicts['hobby'][1])       # ['축구', '농구', '배구'] 에 있는 인덱스 값 1을 출력  | 농구 출력



# 딕셔너리 조회/삽입/수정/삭제
# 컴퓨터 프로그램에서 "CRUD" 라고 부름
# "CRUD" 라는 용어는 개발자의 필수요소
# "CRUD" 는 프로그래밍 뿐만 아니라 데이터 베이스에서도 사용되는 용어
'''
   C: Creative(생성)
   R: Read    (조회)
   U: update  (수정)
   D: Delete  (삭제)
'''


dicContainer ={
     '이름'  : '홍길동',
     '나이'  : 25,
     '주소'  : '대전 중구',
     '취미'  : ['축구','수영','조깅'],
     '몸무게': 87.5
}


# # CRUD C: Creative(추가)

# print(f'dicContaner: {dicContainer}')            

# # 데이터 추가 방법
# # dicContainver[키] = 밸류
                     
# dicContainer['연락처'] = '010-1111-2222'
# print(f'dicContaner: {dicContainer}')                 # 출력 → dicContainer 에서 연락처가 추가된 채로 출력 


# # CRUD R: Read(조회)

# print(f'이름: {dicContainer['이름']}')                # 출력 → 이름: 홍길동
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              

# # CRUD U: Update(수정)

# dicContainer['몸무게'] = 60
# print(f'수정 된 몸무게: {dicContainer['몸무게']}')    # 출력 → 수정 된 몸무게: 60


# # CRUD D: Delet(삭제)

# del dicContainer['몸무게']  
# print(f'dicContaner: {dicContainer}')                # 출력 → dicContainer 에서 몸무개가 삭제된 채로 출력 
       

# # 아이템 갯수 조회
#                                                       # 이름, 나이, 주소, 취미, 연락처 키의 갯수를 파악
# print(f'아이템 갯수: {len(dicContainer)}개')          # 출력 → 아이템 갯수: 5개


# # 전체키 조회                                        # 타입은 dict_keys
# dicKeys = dicContainer.keys()                        # dicKeys = dicContainer 의 키 값만 할당 
# print(f'dicKeys: {dicKeys}')                         # 출력 → dicKeys: dict_keys(['이름', '나이', '주소', '취미', '연락처'])

# for key in dicKeys:
#     print(f'{key} : {dicContainer[key]}')


# # 밸류 조회                                          # 타입은 dict_values
# dicValues = dicContainer.values()
# print(f'dicValues: {dicValues}')


# # 키값과 밸류를 한번에 조회
# for key, value in dicContainer.items():
#     print(f'{key}: {value}')

# items = dicContainer.items()
# print(f'items: {items}')


# for item in items:
#    print(f'item: {item}')
#    print(f'item[0], item[1]: {item[0]}, {item[1]}')


# Quiz) 중간고사 성적 관리 프로그램 만들기
'''
아래 시나리오를 기반으로 딕셔너리를 이용해서 중간고사 성적 관리 프로그램을 만들어봅시다.
 -1 : 중간고사의 성적(C/C++은 A, Java는 B+, 모바일은 C, 보안은 A+, 해킹은 F, 시스템은 C+)을 저장하는 
      딕셔너리를 만든다.
 -2 : 'Java'와 '시스템' 과목의 성적을 조회한다.
 -3 : 추가로 2과목의 성적(파이썬은 A, OS는 A+)을 삽입한다.
 -4 : 'Java'와 '시스템'의 성적을 각각 'F'와 'A'로 수정한다.
 -5 : 전체 과목과 성적을 조회하여 최종 성적표를 출력한다.
'''


# scores = {
#     'C/C++' :'A',
#     'JAVA'  :'B+',
#     '모바일':'C',
#     '보안'  :'A+',
#     '해킹'  :'F',
#     '시스템':'C+'
# }

# # 2 'java'와'시스템의 키값 조회'
# print(f' java : {scores['JAVA']}')
# print(f'시스템: {scores['시스템']}')

# # 3 추가로 2과목의 성적(파이썬은 A, OS는 A+)을 삽입
# scores['파이썬'] = 'A'
# scores['OS'] = 'A+'
# print(f'scores: {scores}')

# # 4 'Java'와 '시스템'의 성적을 각각 'F'와 'A'로 수정
# scores['JAVA'] = 'F'
# scores['시스템'] = 'A'
# print(f'scores: {scores}')


# # 5 전체 과목과 성적을 조회하여 최종 성적표를 출력한다.
# for key in scores.keys():
#     print(f'{key}:\t{scores[key]}')

'''
A+  = 4.5
A   = 4.0
B+  = 3.5
B   = 3.0
C+  = 2.5
C   = 2.0
F   = 0

C/C++ : A     | 4.0          
JAVA  : F     | 0       
모바일: C     | 2.5      
보안  : A+    | 4.5          
해킹  : F     | 0          
시스템: A     | 4.0          
파이썬: A     | 4.0          
OS    : A+    | 4.5          

# '''

# creditsScores = {
#     'A+': 4.5,
#     'A' : 4.0,
#     'B+': 3.5,
#     'B' : 3.0,
#     'C+': 2.5,
#     'C' : 2.0,
#     'F' : 0 
# }
# totalScore = 0
# average = 0
# for key in scores.keys():
#     totalScore += creditsScores[scores[key]]
#     print(f'{key}: {scores[key]}')


# print(f'totalScore: {totalScore}')
# average = totalScore / len(scores)
# print(f'average: {average}')




























































































































































































































