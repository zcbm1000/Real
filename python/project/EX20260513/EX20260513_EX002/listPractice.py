
# Quiz) 출석부 관리 시스템
'''
[[ 시나리오 ]]
1 :  학급 학생수가 10명(정우람, 박으뜸, 배힘찬, 천영웅, 신석기, 배민규, 전민수, 박건우, 박찬호, 이승엽)인 리스트를 만든다.
2 :  ‘가나다’ 순으로 정렬한다.
3 :  ‘박찬호’ 학생이 전학을 가게 되었다. 출석부에서 삭제한 후 전체 학생과 학생 수를 출력한다.
 4 :  선생님을 돕기 위한 학생으로 앞에서 3명을 뽑는다.
 5 :  새로운 친구가 전학 왔다. 이름은 ‘이병규’이다.
 6 :  자리를 바꾸기 위해서 학생 순서를 역순으로 뒤집는다.
 7 :  ‘정우람’ 학생이 이름을 ‘정잘남’으로 개명했다.
 '''

# students = ['정우랑','박으뜸','배힘찬','천영웅','신석기','배민규','전민수','박건우','박찬호','이승엽']
# print(f'students: {len(students)}')       # students 의 아이템 갯수를 출력

# students.sort(reverse=False)              # students 를 오름차순으로 정렬함
# print(f'students: {students}')

# students.remove('박찬호')                 # students 내 '박찬호' 제거
# print(f'students: {students}')
# print(f'students: {len(students)}')       # students 의 아이템 갯수를 출력

# helpers = students[:3]                   # students 내 앞에서부터 3명을 추출
# print(f'4번 정답:{helpers}')

# students.append('이병규')                 # students 에 '이병규' 추가
# students.sort(reverse=False)              # students 오름차순 정렬
# print(f'students: {len(students)}')       

# # import random
# # random.shuffle(students)                # students 를 랜덤으로 지정
# # print(students)                         

# students.index('정우랑')
# idx = students.index('정우랑')
# students[idx] = '정잘남'
# print(f'students: {students}')


# # Quiz) 혈액 보관 시스템
# '''
# 헌혈 프로그램을 통해서 10명의 기부자에게 혈액을 받아 리스트에 보관하고,
# 보관중인 혈액의 혈액형을 각 몇 팩씩 보유중인지 확인할수 있는 프로그램

# '''


# LOOP_COUNT = 10

# blood = []
# for i in range(LOOP_COUNT):                      # range(0:10) 
#     print(f'혈액형을 선택해 주세요. A, B, AB, O')
#     blood.append(input())
# print(f'blood: {blood}')
# print(f' A  형: {blood.count('A')} 개')           # X.conut(Y)  X 리스트 안에 Y개가 몇개인지 카운트함
# print(f' B  형: {blood.count('B')} 개')           # blood 라는 리스트 내에서 B 가 몇개인지 세어줌
# print(f' O  형: {blood.count('O')} 개')
# print(f'A B 형: {blood.count('AB')} 개')














































































































































































































































































































































































































