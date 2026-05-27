# # Quiz) 가위 바위 보 게임

# import random

# pick = ['가위', '바위', '보']

# comPick = random.randint(0, 2)

# userPick = int(input('가위 바위 보를 선택하세요.\n0.가위, 1.바위, 2.보 중 선택하세요.' ))

# print(f'comPick: {pick[comPick]}')
# print(f'userPick: {pick[userPick]}')
# if pick[comPick] == pick[userPick]:
#     print('비김')
    
# elif (userPick == 0 and comPick == 2) or\
#      (userPick == 1 and comPick == 0) or\
#      (userPick == 2 and comPick == 1):
#      print('user 승')
# else:
#      print('com 승')     


#------------------------------------------------------------------

# Quiz) 단어장 중에서 무작위로 출력되는 영어단어를 맞추는 게임
'''
축구   = football
연필   = pencil
지우개 = eraser
자동차 = car
인형   = doll
시계   = clock
'''

import random

words = {
    'football': '축구',
    'pencil'  : '연필',
    'eraser'  : '지우개',
    'car'     : '자동차',
    'doll'    : '인형',
    'clock'   : '시계'
}

attempt = 0


englishWord = random.choice(list(words.keys()))
print(englishWord)

while True:
    userAnswer = input("한글 뜻을 입력하세요: ")
    if userAnswer == words[englishWord]:
        print("정답")
        break
    else:
        attempt +=1

        print("틀렸습니다. 다시 시도해보세요!")
        if attempt >= 3:
        
            print('정답 3회 실패로 끝')
            break






























































































































































































































































































