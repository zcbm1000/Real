# QUiz) 
'''
하루 중 인상 깊었던 일을 파일에한 줄로 작성하는 '한 줄 일기장' 프로그램
'''

'''
import config
from util import getDay, getTime

dFlag = True

while dFlag:
    selectedMenuNum = int(input('메뉴 다음중 선택하세요.\n1. 일기작성   2. 일기조회   0.종료\n선택:'))
    if selectedMenuNum == config.DIARYWRITE:

        print(f'[{getDay()}] 한 줄 일기를 작성하세요.')
        
        todayDiary = input()

        with open('C:\ktk\KTK\python\diary.txt', 'a') as f:
            f.write(f'[{getDay()}] [{getTime()}] {todayDiary}\n')

    elif selectedMenuNum == config.DIARYREAD:
        with open('C:\ktk\KTK\python\diary.txt', 'r') as f:
            str = f.read()
            print(str)

    elif selectedMenuNum == config.SYSTEM_SHUTDOWN:    
        print('Bye')
        dFlag = False
'''


